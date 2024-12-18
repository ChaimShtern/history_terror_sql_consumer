from app.models import Attack, Location, Group, Weapon, Casualty, PropertyDamage, HostageSituation


def parse_and_save(data, session_maker):
    with session_maker() as session:
        all_objects = []
        for item in data:
            # מיקום
            location = Location(
                latitude=item.get('latitude'),
                longitude=item.get('longitude'),
                country=item.get('country_txt'),
                region=item.get('region_txt'),
                city=item.get('city')
            )
            all_objects.append(location)

            # קבוצות
            group_names = [item.get('gname'), item.get('gname2'), item.get('gname3')]
            groups = []
            for group_name in group_names:
                if group_name and group_name != 'nan':
                    group = session.query(Group).filter_by(name=group_name).first()
                    if not group:
                        group = Group(name=group_name,
                                      num_perpetrators=item.get('nperps', 0),
                                      uncertain=item.get('guncertain1', False))
                        all_objects.append(group)
                    groups.append(group)

            # התקיפה
            attack = Attack(
                target_type1=item.get('attacktype1_txt'),
                target_type2=item.get('attacktype2_txt'),
                target_type3=item.get('attacktype3_txt'),
                year=item.get('iyear'),
                month=item.get('imonth'),
                day=item.get('iday'),
                location=location,
                summary=item.get('summary'),
                additional_notes=item.get('addnotes'),
                source1=item.get('scite1'),
                source2=item.get('scite2'),
                source3=item.get('scite3'),
                attack_type1=item.get('attacktype1_txt'),
                attack_type2=item.get('attacktype2_txt'),
                attack_type3=item.get('attacktype3_txt')
            )
            attack.groups = groups
            all_objects.append(attack)

            # כלי נשק
            weapons = [
                (item.get('weaptype1_txt'), item.get('weapsubtype1_txt')),
                (item.get('weaptype2_txt'), item.get('weapsubtype2_txt')),
                (item.get('weaptype3_txt'), item.get('weapsubtype3_txt')),
                (item.get('weaptype4_txt'), item.get('weapsubtype4_txt'))
            ]
            for weapon_type, weapon_subtype in weapons:
                if weapon_type:
                    weapon = Weapon(type=weapon_type, subtype=weapon_subtype, attack=attack)
                    all_objects.append(weapon)

            # נפגעים
            casualty = Casualty(
                killed=item.get('nkill') - item.get('nkillter'),
                wounded=item.get('nwound'),
                attack=attack
            )
            all_objects.append(casualty)

            # נזק לרכוש
            if item.get('property', 0) == 1:
                property_damage = PropertyDamage(
                    property_damaged=True,
                    value=item.get('propvalue'),
                    extent=item.get('propextent_txt'),
                    attack=attack
                )
                all_objects.append(property_damage)

            # חטיפות וסחיטה
            if item.get('ishostkid', 0) == 1:
                hostage_situation = HostageSituation(
                    is_hostage=True,
                    num_hostages=item.get('nhostkid'),
                    ransom=item.get('ransom'),
                    ransom_amount=item.get('ransomamt'),
                    outcome=item.get('hostkidoutcome_txt'),
                    attack=attack
                )
                all_objects.append(hostage_situation)

        # הוספת כל האובייקטים לדאטה בייס
        session.add_all(all_objects)
        session.commit()


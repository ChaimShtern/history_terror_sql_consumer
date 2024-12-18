def insert_many_attacks(session_maker, attacks: list):
    with session_maker() as session:
        try:
            session.add_all(attacks)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occurred: {e}")

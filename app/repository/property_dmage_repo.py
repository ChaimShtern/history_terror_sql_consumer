def insert_many_property_damages(session_maker, property_damages: list):
    with session_maker() as session:
        try:
            session.add_all(property_damages)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occurred: {e}")

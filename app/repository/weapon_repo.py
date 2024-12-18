def insert_many_weapons(session_maker, weapons: list):
    with session_maker() as session:
        try:
            session.add_all(weapons)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occurred: {e}")

def insert_many_locations(session_maker, locations: list):
    with session_maker() as session:
        try:
            session.add_all(locations)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occurred: {e}")

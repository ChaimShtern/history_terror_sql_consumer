def insert_many_casualties(session_maker, casualties: list):
    with session_maker() as session:
        try:
            session.add_all(casualties)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occurred: {e}")

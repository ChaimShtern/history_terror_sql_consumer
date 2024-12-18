def insert_many_groups(session_maker, groups: list):
    with session_maker() as session:
        try:
            session.add_all(groups)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occurred: {e}")

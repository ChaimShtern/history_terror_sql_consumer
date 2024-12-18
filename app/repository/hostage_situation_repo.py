def insert_many_hostage_situations(session_maker, hostage_situations: list):
    with session_maker() as session:
        try:
            session.add_all(hostage_situations)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occurred: {e}")

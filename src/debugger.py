
from adapters.postgres_repository.pet_store import PostgresPetStoreRepo
from pkg.db_sqlalchemy.connection import DB_Params, create_sqlalchemy_engine


def main():
    db_params = DB_Params(
        DB_NAME="postgres",
        DB_USERNAME="postgres",
        DB_PASSWORD="postgres",
        DB_PORT="15432",
        DB_HOST="localhost",
    )
    db_engine = create_sqlalchemy_engine(db_params)
    with PostgresPetStoreRepo(db_engine) as repo:
        pet = repo.get_pet(1)
    print(pet)

if __name__ == "__main__":
    main()

# STANDARD IMPORTS
from decouple import config

# THIRD PART IMPORTS
from loguru import logger

# PROJECT IMPORTS
from src.infrastructure.mongo_db.infrastructure import MongoDBInfrastructure


class LaptopMongoRepository:
    infra = MongoDBInfrastructure
    database = config("MONGODB_DATABASE_NAME")
    collection = config("MONGODB_COLLECTION")

    @classmethod
    def __get_collection(cls):
        mongo_client = cls.infra.get_client()
        try:
            database = mongo_client[cls.database]
            collection = database[cls.collection]
            return collection
        except Exception as error:
            message = (
                f"Repository::__get_collection::Error when trying to get collection"
            )
            logger.error(
                error=error,
                message=message
            )
            raise ValueError

    # @classmethod
    # def save_laptops_on_database(
    #         cls,
    #         laptops: list
    # ) -> bool:
    #
    #     collection = cls.__get_collection()
    #     was_inserted = collection.insert_many(
    #         laptops
    #     )
    #
    #     if not type(was_inserted.inserted_ids) == list:
    #         raise Exception
    #
    #     return bool(was_inserted)

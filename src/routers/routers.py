# STANDARD IMPORTS
from http import HTTPStatus
from aioflask import Flask
from flask import Response
from loguru import logger

# PROJECT IMPORTS
from src.domain.response.response_model import ResponseModel
from src.domain.enums.status_code.enum import InternalCode


app = Flask("Horus API")


@app.route("/put/save_laptops")
async def insert_laptops_on_database() -> Response:
    try:
        response = 0

        response = ResponseModel(
            success=True,
            message="DATA WAS DULLY INSERTED ON DATABASE",
            result=response,
            code=InternalCode.SUCCESS
        ).build_http_response(status=HTTPStatus.OK)
        return response

    except ValueError as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="VALUE ERROR CAUSED BY A RANDOM REASON",
            code=InternalCode.VALUE_ERROR,
        ).build_http_response(status=HTTPStatus.BAD_REQUEST)
        return response

    except Exception as ex:
        logger.error(ex)
        response = ResponseModel(
            success=False,
            message="AN UNEXPECTED ERROR HAS OCCURRED",
            code=InternalCode.INTERNAL_SERVER_ERROR,
        ).build_http_response(status=HTTPStatus.INTERNAL_SERVER_ERROR)
        return response

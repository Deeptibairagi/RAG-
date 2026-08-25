# import sqlite3
# import os

# from config.settings import (
#     DATABASE_PATH
# )


# # ==========================================================
# # CREATE DATABASE DIRECTORY
# # ==========================================================

# def ensure_database_directory():

#     directory = os.path.dirname(
#         DATABASE_PATH
#     )

#     if directory:

#         os.makedirs(
#             directory,
#             exist_ok=True
#         )


# # ==========================================================
# # DATABASE CONNECTION
# # ==========================================================

# def get_connection():

#     ensure_database_directory()

#     return sqlite3.connect(
#         DATABASE_PATH,
#         check_same_thread=False
#     )


import os
import sqlite3

from config.settings import DATABASE_PATH


# ==========================================================
# CREATE DATABASE DIRECTORY
# ==========================================================

def ensure_database_directory():

    directory = os.path.dirname(
        DATABASE_PATH
    )

    if directory:

        os.makedirs(
            directory,
            exist_ok=True
        )


# ==========================================================
# DATABASE CONNECTION
# ==========================================================

def get_connection():

    ensure_database_directory()

    connection = sqlite3.connect(
        DATABASE_PATH,
        check_same_thread=False,
        timeout=30
    )

    return connection
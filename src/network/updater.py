import logging

from src import customlogger as logger


if __name__ == '__main__':
    logging.basicConfig(level=logging.CRITICAL,
                        format='%(asctime)s - %(levelname)s - %(module)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')
    logger.setLevel(logging.DEBUG)
    from src.network import meta_updater

    meta_updater.update_database()
    from src.network import music_updater

    music_updater.update_musicscores()

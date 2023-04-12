import logging
import coloredlogs

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
# Add the handler to the logger
logger.addHandler(console_handler)

# Configure the logger to output color-coded log messages
coloredlogs.install(
    logger=logger,
    fmt='%(asctime)s - %(levelname)s - %(message)s',
    level_styles={
        'debug': {'color': 'green'},
        'info': {'color': 'white'},
        'warning': {'color': 'yellow'},
        'error': {'color': 'red'},
        'critical': {'color': 'red', 'bold': True},
    },
    field_styles={
        'asctime': {'color': 'yellow'},
        'levelname': {'color': 'cyan', 'bold': True},
        'message': {'color': 'black'},
    }
)
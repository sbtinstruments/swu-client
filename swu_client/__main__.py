import aiohttp
import asyncio
import logging
import os
import sys

from pathlib import Path

HOST = os.environ.get("SWU_CLIENT_HOST", "localhost")
try:
    PORT = int(os.environ.get("SWU_CLIENT_PORT"))
except (TypeError, ValueError):  # TypeError if `get` returns None
    PORT = 5011
PATH = os.environ.get("SWU_CLIENT_REMOTE_PATH", "/upload")
URL = os.environ.get("SWU_CLIENT_URL", f"http://{HOST}:{PORT}{PATH}")

_LOGGER = logging.getLogger()
_LOGGER.setLevel(logging.DEBUG)
_LOGGER.addHandler(logging.StreamHandler(sys.stdout))

async def main() -> None:
	# Check "command" argument
	if sys.argv[1] != "send":
		_LOGGER.error("First argument must be 'send'. We don't support other commands.")
		sys.exit(1)
	swu_file = Path(sys.argv[2])
	# Check arguments for the "send" command
	if not swu_file.is_file():
		_LOGGER.error(f"Given SWU is not a file: {swu_file}")
		sys.exit(1)
	# Send the SWU file to swupdate
	try:
		await send_swu_file(swu_file)
	except Exception as exc:
		_LOGGER.error("Something went wrong: {str(exc)}")
		_LOGGER.debug("Reason:", exc_info=exc)
		sys.exit(2)
	_LOGGER.info("Successfully sent SWU file to swupdate.")

async def send_swu_file(swu_file: Path) -> None:
	with swu_file.open("rb") as io:
		_LOGGER.debug(f"Opened SWU file: {swu_file}")
		async with aiohttp.ClientSession() as session:
			_LOGGER.debug("Sending SWU file to swupdate")
			await session.post(URL, data={"file": io})

asyncio.run(main())

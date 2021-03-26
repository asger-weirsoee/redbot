import subprocess
from discord import File

from ProgrammedFeatures.ProgramFeatureClass import Feature


class InspiroBot(Feature):
    def __init__(self, bot):
        super().__init__(bot)

    async def _exec(self, channel, config=None):
        subprocess.getoutput(
            'curl "https://inspirobot.me/api?generate=true" | xargs curl -o ' + config['root'].joinpath(
                'tmp.jpg').__str__())
        vvv = File(config['tmp_folder'].joinpath('tmp.jpg').__str__())
        await channel.send(file=vvv)
        vvv.close()

    def _dummy(self, channel, config=None):
        print(f"Sends file inspiro file")

    @staticmethod
    def _get_name():
        return 'InspiroBot'
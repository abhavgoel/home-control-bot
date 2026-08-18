import asyncio
from pywizlight import wizlight, PilotBuilder

LIGHT_IP = "192.168.1.2"


async def main():
    light = wizlight(LIGHT_IP)

    scenes = await light.getSupportedScenes()

    print(scenes)

    scenes = await light.getSupportedScenes()

    cozy_id = scenes.index("Cozy")
    print(cozy_id)


asyncio.run(main())
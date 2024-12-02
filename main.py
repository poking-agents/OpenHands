import asyncio

from pyhooks import Hooks

from openhands.core.main import (
    generate_sid,
    load_app_config,
    run_controller,
)
from openhands.events.action import MessageAction

hooks = Hooks()


async def main(*args):
    print('STARTING OPENHANDS AGENT')
    task = await hooks.getTask()
    task_string = task.instructions.strip()
    hooks.log('Task:', task_string)

    initial_user_action = MessageAction(content=task_string)
    config = load_app_config(config_file='config.toml')
    session_name = 'openhands-agent'
    sid = generate_sid(config, session_name)

    asyncio.run(
        run_controller(
            config=config,
            initial_user_action=initial_user_action,
            sid=sid,
        )
    )


if __name__ == '__main__':
    hooks.main(main)

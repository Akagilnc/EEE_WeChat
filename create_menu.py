from werobot import WeRoBot
robot = WeRoBot()
robot.config["APP_ID"] = "wx9c5976119b523f2c"
robot.config["APP_SECRET"] = "bee50d69573253dcb7b97f15094d0660"

client = robot.client


def create_menu(robot):
    robot.client.create_menu({
        "button": [
            {
                "type": "click",
                "name": "胡说八道",
                "key": "menu1"
            },
            {
                "type": "click",
                "name": "一起来玩",
                "key": "menu2"
            },
            {
                "type": "click",
                "name": "占个位置",
                "key": "menu3"
            }
        ]
    })


if __name__ == "__main__":
    create_menu(client)

def cut_off(text, words):
    """
    Сокращает текст до указанного количества слов.
    Если текст был сокращен, добавляется суфикс ...
    """
    text = text.split()
    sufix = '...' if len(text) > words else ''
    return " ".join(text[:words]) + sufix


def check_correct_slack_name(nikname):
    """
    Проверят что ник для Slack записано правильно. Например:
    nickname --> @nickname
    @nickname --> @nickname
    @@nickname --> @nickname
    """
    return '@' + nikname.split('@')[-1]


def get_type_to_slack(type):
    if type == 'idea':
        return "новую идею"
    else:
        return "новый проект"


def get_new_project_message(project, employees_list, link):
    employees = []
    for employee in employees_list:
        employees.append({"type": "plain_text", "text": employee})
    return {
        "blocks":
            [
                {
                    "type": "section",
                    "text":
                        {
                            "type": "mrkdwn",
                            "text": f":loudspeaker:   *{check_correct_slack_name(project.slack)} \
                             добавил {get_type_to_slack(project.project_type)} на сайте 21entrepreneurs.ru*"
                        }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text":
                        {
                            "type": "mrkdwn",
                            "text": f"*{project.name}*"
                        }
                },
                {
                    "type": "section",
                    "text":
                        {
                            "type": "plain_text",
                            "text": f"{cut_off(project.description, 30)}",
                            "emoji": True
                        }
                },
                {
                    "type": "context",
                    "elements":
                        [
                            {
                                "type": "plain_text",
                                "text": "Ждём в команду:"
                                , "emoji": True
                            }
                        ]
                },
                {
                    "type": "section",
                    "fields": employees
                },
                {
                    "type": "section",
                    "text":
                        {
                            "type": "mrkdwn",
                            "text": f"<{link}#project{project.id}|_Смотреть целиком_>"
                        }
                }
            ]
    }


def get_new_applicant_message(applicant, link):
    return {
        "blocks":
            [
                {
                    "type": "section",
                    "text":
                        {
                            "type": "mrkdwn",
                            "text": f":bust_in_silhouette:   *{check_correct_slack_name(applicant.slack)} \
                            добавил новую анкету на сайте 21entrepreneurs.ru*"
                        }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "section",
                    "text":
                        {
                            "type": "mrkdwn",
                            "text": f"*{applicant.name}*"
                        }
                },
                {
                    "type": "section",
                    "text":
                        {
                            "type": "plain_text",
                            "text": f"{cut_off(applicant.about_message, 30)}",
                            "emoji": True
                        }
                },
                {
                    "type": "context",
                    "elements":
                        [
                            {
                                "type": "plain_text",
                                "text": "Навыки:"
                                , "emoji": True
                            }
                        ]
                },
                {
                    "type": "section",
                    "text":
                        {
                            "type": "plain_text",
                            "text": f"{applicant.skills}",
                            "emoji": True
                        }
                },
                {
                    "type": "section",
                    "text":
                        {
                            "type": "mrkdwn",
                            "text": f"<{link}#applicant{applicant.id}|_Смотреть целиком_>"
                        }
                }
            ]
    }

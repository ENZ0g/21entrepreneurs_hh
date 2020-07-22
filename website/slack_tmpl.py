def cut_off(text, words):
    text = text.split()
    sufix = '...' if len(text) > words else ''
    return " ".join(text[:words]) + sufix


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
                            "text": ":loudspeaker:   *Новая карточка проекта на сайте 21entreprenuers.ru*"
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
                            "text": ":bust_in_silhouette:   *Новая карточка соискателя на сайте 21entreprenuers.ru*"
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

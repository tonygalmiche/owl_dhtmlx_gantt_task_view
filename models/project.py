# -*- coding: utf-8 -*-
from odoo import models,fields
from datetime import datetime, date, timedelta


class project_task(models.Model):
    _inherit = "project.task"

    def get_dhtmlx(self, domain=[]):
        tasks=self.env['project.task'].search(domain, order="name", limit=500)

        #** Ajout des projets *************************************************
        res=[]
        projects=[]
        for task in tasks:
            if task.project_id not in projects:
                projects.append(task.project_id)
        for project in projects:
            vals={
                "id": project.id+100000,
                "text": "PROJET : %s"%project.name,
                "start_date": False,
                "duration": False,
                "parent": 0,
                "progress": 0,
                "open": True,
                "assigned": project.user_id.name,
                "priority": 2,
            }
            res.append(vals)
        #**********************************************************************

        #** Ajout des taches **************************************************
        for task in tasks:
            vals={
                "id": task.id,
                "text": task.name,
                "end_date": task.date_deadline or datetime.now(),
                "duration": task.planned_hours or 8,
                "parent": task.project_id.id+100000,
                "assigned": task.user_id.name,
                "progress": task.progress/100,
                "priority": int(task.priority),
            }
            res.append(vals)
        #**********************************************************************


        #** Ajout des dependances *********************************************
        links=[]
        ct=1
        for task in tasks:
            if len(task.dependency_task_ids):
                for dependency in task.dependency_task_ids:
                    vals={
                        "id":ct,
                        "source": dependency.id,
                        "target": task.id,
                        "type":0,
                    }
                    links.append(vals)
                    ct+=1
        #**********************************************************************

        return {"items":res, "links": links}

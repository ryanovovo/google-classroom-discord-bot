from classroomCore import get_service


class Classroom:
    def __init__(self):
        self.courses_id = {}
        self.service = get_service()
        self.reload_course_id()

    def list_anc(self, name, size=1):
        self.service = get_service()
        anc = self.service.courses().announcements().list(courseId=self.courses_id[name], pageSize=size).execute()['announcements']
        return anc

    def list_course(self):
        self.service = get_service()
        courses = self.service.courses().list(pageSize=100).execute()['courses']
        return courses

    def list_hw(self, name, size=1):
        self.service = get_service()
        hw = self.service.courses().courseWork().list(courseId=self.courses_id[name], pageSize=size).execute()['courseWork']
        return hw

    #def get_latest_anc(self):


    def reload_course_id(self):
        self.service = get_service()
        courses = self.list_course()
        for course in courses:
            self.courses_id[course['name']] = course['id']




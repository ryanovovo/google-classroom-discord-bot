from classroomCore import get_service


class Classroom:
    def __init__(self):
        self.courses_id = {}
        self.service = get_service()
        self.reload_course_id()

    def list_anc(self, name, size=1):
        self.service = get_service()
        # self.reload_course_id()
        anc = self.service.courses().announcements().list(courseId=self.courses_id[name], pageSize=size).execute()
        anc = anc.get('announcements', [])
        return anc

    def list_course(self):
        self.service = get_service()
        # self.reload_course_id()
        courses = self.service.courses().list().execute()
        courses = courses.get('courses', [])
        return courses

    def list_hw(self, name, size=1):
        self.service = get_service()
        # self.reload_course_id()
        hw = self.service.courses().courseWork().list(courseId=self.courses_id[name], pageSize=size).execute()
        hw = hw.get('courseWork', [])
        return hw

    def reload_course_id(self):
        self.service = get_service()
        courses = self.list_course()
        for course in courses:
            self.courses_id[course['name']] = course['id']




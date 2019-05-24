from member.model import MemberDAO


class MemberController:

    def __init__(self):
        self.dao = MemberDAO()

    def login(self,userid, password):

        row = self.dao.login(userid, password)
        view = ''
        if row is None:
            view = 'index.html'
        else:
            view = 'home.html'
        return view


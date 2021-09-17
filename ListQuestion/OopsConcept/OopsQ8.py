#DUck typing : Here we eill prove that if function behave like function A and then we call called that function A . : EG of duck if bird behvae like duck like swim and all then we call bird as duck

class pyCharm:
    def execute(self):
        print("Compiling ")
        print("Running ")

class laptop:
    def code(self,ide):
        ide.execute()

class myCharm:
    def execute(self): 
        print("Eat ")
        print("Swim")
        print("sleep")
        print("travel ")



ide = myCharm()  # Here it prove myCharm has execute function so it will behav elike pyCharm by passingide in it
ide = pyCharm()  
lap1 = laptop()
lap1.code(ide)
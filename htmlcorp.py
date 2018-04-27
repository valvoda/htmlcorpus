import os

class Html:

    def makeIndex(self, path):
        index = open("index.html", "w")

        links = []
        for filename in os.listdir(path):
            if filename.endswith(".txt"):
                name = filename.split(".txt")[0]
                links.append(name)

        links.sort(key=int)
        for link in links:
            index.write("<p><a href='/corpus/" + link + "'>" + link + "</a></p>")

    def openFiles(self, path):

        for filename in os.listdir(path):
            if filename.endswith(".txt"):
                name = filename.split(".txt")[0]
                case = open(path + "/" + filename, "r")
                self.makeHtml(case, name)

    def makeHtml(self, case, filename):

        htmlcase = open("htmlcorpus/" + filename + ".html", "w")
        self.writeTop(filename, htmlcase)

        content = case.readlines()
        content = [x.strip() for x in content]

        judges = self.getJudges(content)

        linecount = 0
        for line in content:
            self.writeLine(line, linecount, htmlcase)
            linecount += 1

        htmlcase.write("<p> Who forms the majority? </p>")

        for judge in judges:
            self.writeJudge(judge, htmlcase)

        htmlcase.write("<input type='submit' value='Submit'>")

        htmlcase.write("</form>")

        self.writeEnd(htmlcase)

    def writeEnd(self, htmlcase):
        end = "<br><a type='button' href='/logout'>Logout</a>\
        </body>\
        </html>"

        htmlcase.write(end)

    def writeTop(self, filename, htmlcase):
        top = "<!DOCTYPE html> \
        <html> \
        <body> \
        <form action='/concurrence' method='post'> \
        <input type='hidden' name='casenumber' value="

        htmlcase.write(top + "'" + filename + "'>")

    def writeLine(self, line, linecount, htmlcase):
        start = "<input type='checkbox' name='line' value="
        end = "<br>"

        linecount = "'" + str(linecount) + "'"
        htmlcase.write(start + linecount + ">" + line + end + "\n")

    def writeJudge(self, judge, htmlcase):
        start = "<input type='checkbox' name='judge' value ="
        end = "<br>"

        j = "'" + judge + "'" + ">"
        htmlcase.write(start + j + judge + end)

    def getJudges(self, content):
        judges = []
        for i in range(len(content)):
            if content[i] == "-------------NEW JUDGE---------------":
                judges.append(content[i+1])

        return judges

if __name__ == "__main__":

    html = Html()
    html.openFiles("corpus") # To make htmlcorpus
    # html.makeIndex("corpus")

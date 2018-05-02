"""
Decode takes original corpus and annotated corpus as inputs
and finds all the sentences annotated as concurrences.

All the files without annotation are flagged as Errors and missing
concurrences are flagged as warnings.
"""

import os

class Decode:

    def decode_anno(self, anopath, ogpath):
        names, files = self.get_anno(anopath)

        # for file and name in range of list files
        for i in range(len(files)):
            linenum = self.ext_linenums(files[i])
            name = names[i]

            if self.check_anno(name, linenum, files[i]):
                lines = self.get_lines(linenum, name, ogpath) # get sent. corresponding to linenum
                for line in lines:
                    print(line)

            i += 1 #move to another file

    def get_lines(self, linenum, name, ogpath):
        ognames, ogfiles = self.get_anno(ogpath)
        lines = []
        for i in range(len(ogfiles)):
            if ognames[i] == name:
                f = ogfiles[i]
                for l in linenum:
                    lines.append(f[int(l)])

        return lines

    def get_anno(self, path):
        files = []
        names = []

        for fname in os.listdir(path):
            if fname.endswith(".txt"):
                with open(path + "/" + fname) as f:
                    content = f.readlines()
                    content = [x.strip() for x in content]
                    files.append(content)
                    names.append(fname)

        return names, files

    def ext_linenums(self, anno):
        linenum = []
        for l in anno:
            if l.isdigit():
                linenum.append(l)

        return linenum

    def check_anno(self, name, linenum, files):
        if not linenum:
            print("Warning: No lines annotated in: ", name)
        if not files:
            print("ERROR: No MJ in file: ", name)
            return False
        else:
            return True


if __name__ == '__main__':
    dc = Decode()
    anno = "annotated/jv"
    original = "corpus"
    dc.decode_anno(anno, original)

from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get("https://ucsd.edu/academics/academics-detail.html").text
soup = BeautifulSoup(source, "lxml")

subjectList = soup.find_all("ul", class_="list-unstyled")

all_majors = []
for subject in subjectList:
    subject_majors = []
    majors = subject.find_all("li")
    for major in majors[1:]:
        subject_majors.append(major.text)
    all_majors.append(subject_majors)

del all_majors[0:6]

print(all_majors)


subjects = []
subjects_href = []
for subject in subjectList:
        subjects.append(subject.a.text)
        if subject.a.get("href") == "":
            subjects_href.append("None")
        else:
            subjects_href.append(subject.a.get("href"))


del subjects[0:6]
del subjects_href[0:6]
print(subjects)
print(subjects_href)

final_array = []

for subject, majors, link in zip(subjects, all_majors,  subjects_href):
    final_array.append({"subject": subject, "majors": majors, "link": link})

df = pd.DataFrame(final_array)

print(df)

df.to_csv("sandiego.csv")
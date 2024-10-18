import pandas as pd
import re

resumes = pd.read_csv('resumes.csv')
resumes.sample(3)

candidates_df = pd.DataFrame(columns=['id', 'job_title', 'tech_skills', 'education'])       # create new dataframe

for ind in resumes.index:

    position = re.findall(r"[\s+?](\w{1,})", resumes["Resume_str"][ind])                    # extract position
    tech_skills = re.findall(r"\b(Python|SQL|Excel|R)\b", resumes["Resume_str"][ind])       # extract technocal skills
    education = re.findall(r"\b(PhD|Master|Bachelor)\b", resumes["Resume_str"][ind])        # rextract education

    if len(position) > 0 and len(tech_skills) > 0 and len(education) > 0:

        new_record = {                              # if all extracted fields contain information, create a new recordset
            "id": int(resumes['ID'][ind]),
            "job_title": [f"{position[0]} {position[1]}"],
            "tech_skills": [tech_skills],
            "education": [education]
        }

        print(new_record)

        candidates_df.loc[len(candidates_df)] = new_record


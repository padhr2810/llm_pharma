
import gradio as gr
import sqlite3


# for the custom css, you have to look at the inspector console to figure out how to target your elements correctly. 
# And, if you use custom classes, you may have to use "!important" for specificity
# However, custom css isn't a recommended approach in Gradio and it may not work consistently across Gradio versions. 
# What we recommend instead is to use themes: https://gradio.app/theming-guide/
# Example of custom styling with !important
# 	css = """
#	    #warning {background: red;} 
# 	    .feedback {font-size: 24px !important;}
#	    .feedback textarea {font-size: 24px !important;}
#	"""

con = sqlite3.connect("qn.db")	# creates db if doesn't exist.
cur = con.cursor()


# creates table if doesn't exist.
res = cur.execute("SELECT name FROM sqlite_master WHERE name='qn'")
print(f"res = {res}")
found_this_table = res.fetchone()
print(f"res.fetchone() = {found_this_table}")

if found_this_table is None:
    cur.execute("CREATE TABLE qn(age, sex, diagnoses, meds)")
elif found_this_table[0] == "qn":
    print("\n### Table qn exists already.\n")


# We can verify that the new table has been created by querying the sqlite_master table built-in to SQLite, which should now contain an entry for the movie table definition
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()

# Now, add two rows of data supplied as SQL literals:
cur.execute("""
    INSERT INTO qn VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2, "X"),
        ('And Now for Something Completely Different', 1971, 7.5, "X")
""")
con.commit()

res = cur.execute("SELECT age FROM qn")
print(f"all ages = \n{res.fetchall()}")

for i, row in enumerate(cur.execute("SELECT age, sex, diagnoses, meds FROM qn ORDER BY age")):
    print(f"{i+1} = {row}")
    

qs = {
    "Age" : "What is your age?",
    "sex" : ["What is your sex?", ["Male", "Female"]],
    "Diagnoses" : "Do you have any medical diagnosis? Please list any diagnosis here",
    "Medication": "Do you take any medicines? Please list your medicines here."
}

def submit_fn(m, d, a, s):
    # check if all values have been filled out
    # if YES = then push data to sql
    # if NO = then popup - please fill in missing data ... 
    print("Running function submit_fn") 
    print(f"inputs = {m, d, a, s}")

# FFCCCB

css = """
#buttonok {background : #007FFF; color : white}
"""


with gr.Blocks(css=css) as demo:
    text_meds = gr.Textbox(label="Do you take any medicines? Please list your medicines here.")
    text_diag = gr.Textbox(label="Do you have any medical diagnosis? Please list any diagnosis here")
    text_age  = gr.Textbox(label="What is your age?")
    choose_sex = gr.Radio(["Male", "Female"], label="Sex")
    
    submit_button = gr.Button(value="Submit", elem_id="buttonok")
    reset_button  = gr.Button(value="Reset", elem_id="reset_button")
    
    submit_button.click(submit_fn, inputs=[text_meds, text_diag, text_age, choose_sex])
    
    print(f"Sex = {choose_sex}")

    # choose_sex = gr.Dropdown(label="What is your sex?", choices=["Male", "Female"], value=None)

demo.launch()



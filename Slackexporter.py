import os
import json
import datetime
# for slack messages
# Made by Anshul Thakur
# Copyrights Ghost

def daemon_ghost():
    print("""|| ))      ||______                 ||                 ||         ||          _________        ||||||||||  ________________
             ||  ))     ||      |              ||                   ||         ||        (          )       ||                 ||
             ||   ))    ||      |            ||                     ||         ||      (             )      ||                 ||
             ||    ))   ||______|           ||                      ||         ||     (               )     ||                 ||
             ||     ))  ||\\                ||                      ||         ||    (                 )    ||                 ||
             ||     ))  ||  \\              ||                      ||---------||    (                 )    |||||||||||        ||
             ||     ))  ||    \\            ||         |||||||||    ||         ||     (                )             ||        ||
             ||    ))   ||      \\           ||            ||       ||         ||      (              )              ||        ||
             ||   ))    ||        \\     __   ||           ||       ||         ||       (            )               ||        ||
             || ))      ||          \\  |  |   |||||||||||||||      ||         ||        (__________)       |||||||||||        ||
             ||""")

def json_to_htm():
    list_file = os.listdir()
    if len(list_file) != 0:
        fil.write("<H3>")
        fil.write("#" + var.capitalize())
        fil.write("</H3>")
        fil.write("<br>")
        for files in list_file:
            file = open(files, "r")
            message_s = json.load(file)
            fil.write("<center>")
            fil.write("-"*80)
            fil.write(""+files.split(".")[0]+""+'\n')
            fil.write("-"*80)
            fil.write("</center>")
            for varl in message_s:
                if 'text' in varl:
                    if 'user' in varl:
                        if '@' in varl['text']:
                            i = 1
                            str1 = varl['text'].split("<")
                            length = len(str1)
                            str_n = str1[0]
                            while i <= length-1:
                                if '@' in str1[i]:
                                    str_p0 = str1[i].split(">")
                                    str_p0[0] = "<font color = blue>"'@' + user_s_message(str_p0[0].split("@")[1]).capitalize() + " "+"</font>"
                                    str_n += (str_p0[0] + str_p0[1])
                                i += 1
                            fil.write("<p>")
                            fil.write("<b>")
                            fil.write(user_s_message(varl['user']).capitalize() + "\n")
                            fil.write("<font size=1 color = grey>")
                            fil.write(get_timestamp(varl['ts']))
                            fil.write("</font>")
                            fil.write("</b>")
                            fil.write("<br>")
                            fil.write(str_n + '\n')
                            fil.write("</p>")
                        else:
                            fil.write("<p>")
                            fil.write("<b>")
                            fil.write(user_s_message(varl['user']).capitalize() + "\n")
                            fil.write("<font size=1 color = grey>")
                            fil.write(get_timestamp(varl['ts']))
                            fil.write("</font>")
                            fil.write("</b>")
                            fil.write("<br>")
                            fil.write(varl['text'] + '\n')
                            fil.write("</p>")
                    else:
                        print()

                else:
                    print()


def user_s_message(user_id):
    os.chdir("C:\\Users\Vijay\Desktop\pyproj")
    us_file = open("users.json", "r")
    usr = json.load(us_file)
    for war in usr:
        if user_id == war['id']:
            username = war['name']
            break
    os.chdir(var)
    return username


def get_timestamp(timestamp):
    hour = datetime.datetime.fromtimestamp(float(timestamp)).hour
    minutes = datetime.datetime.fromtimestamp(float(timestamp)).minute
    time = str(hour)+":"+str(minutes)
    return time


def html_opening():
    fil.write("<Html>" + '\n')
    fil.write("<Head>")
    fil.write("<Title>")
    fil.write("Slack_expo")
    fil.write("</Title>" + '\n')
    fil.write("</Head>" + '\n')
    fil.write("<Body>")


def html_closing():
    fil.write("</Body>" + '\n')
    fil.write("</Html>")


os.chdir("C:\\Users\Vijay\Desktop\pyproj")
list_Dict = os.listdir()
fil = open("slack_export.html", "w")
html_opening()
for var in list_Dict:
    if os.path.isdir(var):
        os.chdir(var)
        json_to_py()
        os.chdir("C:\\Users\Vijay\Desktop\pyproj")
html_closing()
fil.close()

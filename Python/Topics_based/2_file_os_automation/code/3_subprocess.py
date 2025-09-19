import subprocess

result = subprocess.run(["echo", "Hello Babu"], capture_output=True, text=True)
print(result.stdout)

subprocess.run("ls -ltr", shell=True)

#Check the exit codes
r = subprocess.run(["ls", "/nonexistent"], capture_output=True, text=True)
print(r.returncode)
print(r.stderr)

# Piping
p1 = subprocess.Popen(["ls"],stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "shut"], stdin=p1.stdout, stdout=subprocess.PIPE)
out, _ = p2.communicate()
print(out.decode())
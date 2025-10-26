<h1 align="center">🗂️ Task Manager (CLI Edition)</h1>

<p align="center">
  <b>A simple yet powerful command-line task management system built with Python.</b><br>
  Easily add, modify, complete, delete, and view tasks — all from your terminal.
</p>

---

<h2>📘 Project Overview</h2>

<p>
This <b>Task Manager CLI</b> is a Python-based personal productivity tool that helps you manage your daily to-do items from the command line.
It automatically adjusts task priorities as deadlines approach and stores all data locally in a <code>tasks.json</code> file, so your progress is always saved between sessions.
</p>

---

<h2>⚙️ Features</h2>

<ul>
  <li>✅ <b>Add New Tasks</b> with title, description, priority, and due date/time</li>
  <li>✏️ <b>Modify Existing Tasks</b> (title, due date, description, or priority)</li>
  <li>📅 <b>Automatic Priority Adjustment</b> as deadlines approach</li>
  <li>✔️ <b>Mark Tasks as Complete</b></li>
  <li>🗑️ <b>Delete Tasks</b> (with confirmation prompts)</li>
  <li>📜 <b>View All Tasks</b> sorted by priority and due date</li>
  <li>💾 <b>Persistent Storage</b> using JSON (no external database required)</li>
  <li>🔊 <b>Audio Feedback</b> for errors and successes (cross-platform support)</li>
</ul>

---

<h2>🧩 Folder Structure</h2>

<pre>
TaskManager/
│
├── task_manager.py     # Main script (this file)
├── README.md           # Project documentation
└── LICENCE             # MIT Licence

</pre>

---

<h2>🚀 How to Run</h2>

<ol>
  <li><b>Make sure you have Python 3 installed.</b></li>
  <li>Download or clone this repository:
    <pre>git clone https://github.com/YourUsername/TaskManager.git</pre>
  </li>
  <li>Navigate into the project folder:
    <pre>cd TaskManager</pre>
  </li>
  <li>Run the program:
    <pre>python task_manager.py</pre>
  </li>
</ol>

---

<h2>🖥️ Usage Guide</h2>

<p>Once you run the program, the main menu will appear with the following options:</p>

<pre>
1. Add New Task
2. Modify a Task
3. Mark Task as Complete
4. Delete a Task
5. View All Tasks
6. Close Application
</pre>

<p>
Type the number corresponding to your choice, and follow the prompts.
When adding tasks, you can type <code>menu</code> at any time to abort and return to the main menu.
</p>

---

<h2>📂 Data Storage</h2>

<p>
All tasks are stored in <code>tasks.json</code> automatically. Example structure:
</p>

<pre>
{
  "tasks": [
    {
      "id": 1,
      "title": "Complete Project",
      "priority": "High",
      "description": "Finish Python CLI task manager",
      "due_date": "26-10-2025 14:00",
      "completed": false
    }
  ]
}
</pre>

---

<h2>🧠 Priority System</h2>

<p>
The program uses an automatic priority adjustment system:
</p>

<ul>
  <li>📅 <b>1 Day before due date:</b> Priority increases by 1 level</li>
  <li>⏰ <b>1 Hour before due date:</b> Priority increases again by 1 level (max = High)</li>
</ul>

---

<h2>🔊 Platform Compatibility</h2>

<p>
The script runs on:
</p>

<ul>
  <li>🪟 Windows (with sound via <code>winsound</code>)</li>
  <li>🐧 Linux & macOS (with ASCII bell alerts)</li>
</ul>

---

<h2>🧰 Requirements</h2>

<ul>
  <li>Python 3.x</li>
  <li>No external libraries required — fully built using Python’s standard library</li>
</ul>

---

<h2>📄 Licence</h2>

<p>
  This project is licenced under the <b>MIT Licence</b> — see the <a href="./LICENCE">LICENCE</a> file for details.
</p>

<pre>
MIT Licence

Copyright (c) 2025 Sheikh Hussain

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</pre>


---

<h2>💡 Author</h2>

<p>
👤 <b>Sheikh</b><br>
💬 Learning to Code | Passionate about building clean, functional tools in Python<br>
📧 Email: <i>[your.email@example.com]</i>
</p>

---

<h2 align="center">⭐ If you like this project, please give it a star on GitHub!</h2>

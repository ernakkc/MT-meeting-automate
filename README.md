<hr>
<h1>MT Meeting Automation</h1>
<p>MT Meeting Automation is a Python-based tool designed to automate the process of joining and exiting Microsoft Teams meetings at scheduled times. The tool uses Selenium WebDriver to interact with the Teams web interface and can be configured to join and leave meetings based on a schedule specified in a configuration file.</p>

<h2>Features</h2>
<ul>
  <li><strong>Automated Meeting Entry and Exit:</strong> Join and leave Microsoft Teams meetings automatically at specified times.</li>
  <li><strong>Configuration via INI File:</strong> Easily customize your schedule and account details using a simple INI configuration file.</li>
  <li><strong>Logging:</strong> Detailed logging of all actions and events for troubleshooting and record-keeping.</li>
  <li><strong>Customizable WebDriver Options:</strong> Pre-configured Chrome WebDriver with options to handle notifications, popups, and media permissions.</li>
</ul>

<h2>Installation</h2>

<h3>Prerequisites</h3>
<ul>
  <li>Python 3.6+</li>
  <li>Google Chrome browser installed</li>
</ul>

<h3>Dependencies</h3>
<p>All required Python packages are listed in <code>requirements.txt</code>. To install the dependencies, run:</p>
<pre><code class="!whitespace-pre hljs language-sh">pip install -r requirements.txt</code></pre>

<h3>Required Files</h3>
<p>Ensure the following files are in your project directory:</p>
<ul>
  <li><code>main.py</code>: The main script for the automation tool.</li>
  <li><code>config.ini</code>: The configuration file with your account details, schedule, and settings.</li>
  <li><code>requirements.txt</code>: List of Python package dependencies.</li>
</ul>

<h2>Configuration</h2>
<p>The behavior of the tool is controlled via the <code>config.ini</code> file. Below is a sample configuration:</p>
<pre><code class="!whitespace-pre hljs language-ini">[Account]
name = Eren
surname = Akkoç

[Times]
enter_times = 09.00, 10.30, 12.00, 13.30
exit_times = 10.20, 11.50, 13.20, 14.50

[Settings]
tryNow = False

[Lesson]
link = "https://teams.microsoft.com/l/meetup-join/example_link"</code></pre>

<h3>Configuration Details</h3>
<ul>
  <li><strong>Account:</strong>
    <ul>
      <li><code>name</code>: Your first name.</li>
      <li><code>surname</code>: Your surname.</li>
    </ul>
  </li>
  <li><strong>Times:</strong>
    <ul>
      <li><code>enter_times</code>: Comma-separated list of times (HH.MM format) to join meetings.</li>
      <li><code>exit_times</code>: Comma-separated list of times (HH.MM format) to leave meetings.</li>
    </ul>
  </li>
  <li><strong>Settings:</strong>
    <ul>
      <li><code>tryNow</code>: Set to <code>True</code> to join the meeting immediately after starting the program for testing purposes.</li>
    </ul>
  </li>
  <li><strong>Lesson:</strong>
    <ul>
      <li><code>link</code>: The URL of the Microsoft Teams meeting to join.</li>
    </ul>
  </li>
</ul>

<h2>Usage</h2>
<p>To start the automation tool, simply run the <code>main.py</code> script:</p>
<pre><code class="!whitespace-pre hljs language-sh">python main.py</code></pre>
<p>The tool will read the configuration file, set up the Chrome WebDriver, and begin monitoring the schedule to join and leave meetings at the specified times.</p>

<h3>Logging</h3>
<p>Logs are stored in the <code>logs</code> directory with detailed information about the program's actions and any errors encountered. The log file is named <code>automation_log.log</code>.</p>

<h2>Code Overview</h2>
<h3>main.py</h3>
<p>The <code>main.py</code> script contains the <code>AutoEnter</code> class, which handles reading the configuration file, setting up the WebDriver, and performing the automated actions.</p>
<ul>
  <li><strong>readConfig</strong>: Reads and parses the configuration file.</li>
  <li><strong>setDriver</strong>: Sets up the Chrome WebDriver with the necessary options.</li>
  <li><strong>enterLesson</strong>: Joins the Microsoft Teams meeting.</li>
  <li><strong>exitLesson</strong>: Leaves the Microsoft Teams meeting.</li>
  <li><strong>main</strong>: The main loop that monitors the time and triggers the <code>enterLesson</code> and <code>exitLesson</code> methods at the specified times.</li>
</ul>

<h2>Dependencies</h2>
<p>Make sure to include all required dependencies in <code>requirements.txt</code>:</p>
<pre><code class="!whitespace-pre hljs language-txt">webdriver-manager
selenium
configparser</code></pre>
<p>If you discover any missing dependencies during setup, add them to this list and run <code>pip install -r requirements.txt</code> again.</p>

<h2>Contributing</h2>
<p>Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request on GitHub.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>

<h2>Acknowledgments</h2>
<p>Special thanks to the creators of Selenium and WebDriver Manager for their fantastic tools that make this project possible.</p>
<hr>

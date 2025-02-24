package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"os/exec"
	"runtime"
	"sync"

	"github.com/fatih/color"
)

type Result struct {
	URL   string `json:"url"`
	State string `json:"state"`
}

func main() {
	clearScreen()

	var target string

	fmt.Print("Enter the target link (e.g., https://example.com/): ")
	fmt.Scanln(&target)

	var wg sync.WaitGroup

	directories := []string{"admin.php", "admin1.php", "admin1.html", "admin2.php", "admin2.html", "yonetim.php", "yonetim.html",
		"yonetici.php", "yonetici.html", "ccms/", "ccms/login.php", "ccms/index.php",
		"maintenance/", "webmaster/", "adm/", "configuration/", "configure/", "websvn/", "admin/",
		"admin/account.php", "admin/account.html", "admin/index.php", "admin/index.html", "admin/login.php",
		"admin/login.html", "admin/home.php", "admin/controlpanel.html", "admin/controlpanel.php",
		"admin.html", "admin/cp.php", "admin/cp.html", "cp.php", "cp.html", "administrator/",
		"administrator/index.html", "administrator/index.php", "administrator/login.html", "administrator/login.php",
		"administrator/account.html", "administrator/account.php", "administrator.php", "administrator.html",
		"modelsearch/login.php", "moderator.php", "moderator.html", "moderator/login.php", "moderator/login.html",
		"moderator/admin.php", "moderator/admin.html", "moderator/", "controlpanel/", "controlpanel.php",
		"controlpanel.html", "admincontrol.php", "admincontrol.html", "adminpanel.php", "adminpanel.html",
		"admin1.asp", "admin2.asp", "yonetim.asp", "yonetici.asp", "admin/account.asp", "admin/index.asp",
		"admin/login.asp", "admin/home.asp", "admin/controlpanel.asp", "admin.asp", "admin/cp.asp", "cp.asp",
		"administrator/index.asp", "administrator/login.asp", "administrator/account.asp", "administrator.asp",
		"modelsearch/login.asp", "moderator.asp", "moderator/login.asp", "moderator/admin.asp", "controlpanel.asp",
		"admincontrol.asp", "adminpanel.asp", "fileadmin/", "fileadmin.php", "fileadmin.asp", "fileadmin.html",
		"administration/", "administration.php", "administration.html", "sysadmin.php", "sysadmin.html",
		"phpmyadmin/", "myadmin/", "sysadmin.asp", "sysadmin/", "ur-admin.asp", "ur-admin.php", "ur-admin.html",
		"ur-admin/", "Server.php", "Server.html", "Server.asp", "Server/", "wp-admin/", "administr8.php",
		"administr8.html", "administr8/", "administr8.asp", "webadmin/", "webadmin.php", "webadmin.asp",
		"webadmin.html", "administratie/", "admins/", "admins.php", "admins.asp", "admins.html", "administrivia/",
		"Database_Administration/", "WebAdmin/", "useradmin/", "sysadmins/", "admin1/", "system-administration/",
		"administrators/", "pgadmin/", "directadmin/", "staradmin/", "ServerAdministrator/", "SysAdmin/",
		"administer/", "LiveUser_Admin/", "sys-admin/", "typo3/", "panel/", "cpanel/", "cPanel/", "cpanel_file/",
		"platz_login/", "rcLogin/", "blogindex/", "formslogin/", "autologin/", "support_login/", "meta_login/",
		"manuallogin/", "simpleLogin/", "loginflat/", "utility_login/", "showlogin/", "memlogin/", "members/",
		"login-redirect/", "sub-login/", "wp-login/", "login1/", "dir-login/", "login_db/", "smblogin/", "admin_area/",
		"bigadmin/", "project-admins/", "phppgadmin/", "pureadmin/", "sql-admin/", "radmind/", "openvpnadmin/",
		"wizmysqladmin/", "vadmind/", "ezsqliteadmin/", "hpwebjetadmin/", "newsadmin/", "adminpro/",
		"Lotus_Domino_Admin/", "bbadmin/", "vmailadmin/", "Indy_admin/", "ccp14admin/", "irc-macadmin/",
		"banneradmin/", "sshadmin/", "phpldapadmin/", "macadmin/", "administratoraccounts/", "admin4_account/",
		"admin4_colon/", "radmind-1/", "Super-Admin/", "AdminTools/", "cmsadmin/", "SysAdmin2/", "globes_admin/",
		"cadmins/", "phpSQLiteAdmin/", "navSiteAdmin/", "server_admin_small/", "logo_sysadmin/",
		"database_administration/", "power_user/", "system_administration/", "ss_vms_admin_sm/", "admins",
		"adm", "admin", "administration", "administrator", "administrators", "database", "admin.php", "admin.asp",
		"administrator.php", "administrator.asp", "administrators.asp", "administrators.asp", "login.php", "login.asp",
		"logon.asp", "logon.php", "quanly.asp", "quanly.php", "quantri.php", "quantri.asp", "quantriweb.asp",
		"quantriweb.asp", "admin_index.asp", "admin_index.php", "dangnhap.asp", "dangnhap.php", "phpinfo.", "logs.",
		"log.", "adminwww", "db.", "admin_file", "admin_files", "admin_login", "cpg", "inc_lib", "inc_conf",
		"inc_config", "lib_config", "diendan", "restricted", "forum1", "forum2", "forum3", "diendan1", "diendan2",
		"diendan3", "php", "phpbb", "awstats", "img-sys", "cgi-sys", "java-sys", "php-sys", "adserver", "login-sys",
		"admin-sys", "community", "cgi-sys/mchat.", "temp", "tmp", "ibf", "ipb", "vbb", "vbb1", "vbb2", "adminp",
		"vbb3", "CHANGELOG", "phpMyAdmin", "phpbb1", "phpbb2", "phpBB", "phpBB2", "PHPBB", "hackconkec", "12931293",
		"secret", "root", "cgi-bin", "nobody", "home", "manager", "manage", "live", "exec", "livehelp", "livechat",
		"phplive", "php.", "ko", "khong", "khongdungnua", "kodungnua", "vut", "cuc", "cut", "db", "data", "site",
		"cgi", "taolao", "class", "online", "common", "thesun", "console", "cp", "admincp", "web", "modules",
		"_admin", "_admin_file", "admin_site", "_login", "access", "pass", "admin_user", "admin_users", "cvv",
		"cvv2", "webalizer", "nhanvien", "domain", "mysql", "4rum", "phpmyadmin", "admin_", "login_", "webmaster",
		"webmanager", "quanly", "portal", "server", "seucre", "admin_security", "adm_sec", "admin_sec", "sysuser",
		"mgr", "webcart", "zorum", "phorum", "log", "adminlogs", "adminlog", "logs", "asp", "jsp", "client", "connect",
		"dbase", "dir", "directory", "fileadmin", "hidden", "htdocs", "www", "config", "configuration", "bbs", "webdata",
		"weblog", "weblogs", "webdb", "wwwboard", "wwwforum", "wwwadmin", "wwwsite", "xxx", "xxx2", "vn", "phanmem", "modcp",
		"kernel", "hackdicon", "hackweb", "tut", "nhac", "nghenhac", "amnhac", "thethao", "cache", "vi", "rum", "win",
		"windows", "nix", "slax", "su", "sub", "nano", "linux", "myadmin", "siteadmin", "phpadmin", "phplogin", "errorlog",
		"error_log", "cfg", "pear", "apche", "iis", "generic", "netapp", "netscape", "base", "bugs", "cfdocs", "cgi-local",
		"custdata", "cutenews", "databases", "datas", "dbs", "dc", "adc", "debug", "edit", "eventum", "etc", "firewall",
		"quantri", "gb", "hostadmin", "inc", "mambo", "giaitri", "shell", "msadm", "myphpnuke", "phpnuke", "nuke", "phpwebsite",
		"pls", "helpdesk", "postnuke", "power", "servlet", "session", "shoutbox", "datadump", "dump", "dbdump", "ssl",
		"supporter", "syshelp", "us", "vbulletin", "viewimg", "webtools", "xsql", "accounting", "advwebadmin", "agent",
		"backup", "beta", "ccbill", "cert", "certificate", "doc-html", "dat", "exe", "ftp", "phpmyreport", "vitual",
		"vitualpath", "internal", "intranet", "lan", "wan", "scr", "temporal", "stat", "webstat", "webadmin", "web_admin",
		"webmaster_logs", "filemgmt", "management", "admmgmt", "adm_mgmt", "exp", "expl", "exploit", "exploits", "acp"}

	successFile, err := os.Create("success_urls.json")
	if err != nil {
		fmt.Println("Failed to create file:", err)
		return
	}
	defer successFile.Close()

	encoder := json.NewEncoder(successFile)
	encoder.SetIndent("", "    ")

	for _, dir := range directories {
		wg.Add(1)
		go func(dir string) {
			defer wg.Done()
			url := target + dir

			req, err := http.NewRequest("GET", url, nil)
			if err != nil {
				color.Red(fmt.Sprintf("[-] Error creating request: %v\n", err))
				return
			}
			req.Header.Set("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
			resp, err := http.DefaultClient.Do(req)
			if err != nil || resp.StatusCode != http.StatusOK {
				color.Red(fmt.Sprintf("[-] Unsuccessful admin panel: %s\n", url))
			} else {
				color.Green(fmt.Sprintf("[+] Successful admin panel: %s\n", url))

				result := Result{URL: url, State: "success"}
				err := encoder.Encode(result)
				if err != nil {
					fmt.Println("Failed to write to JSON file:", err)
				}
			}
		}(dir)
	}

	wg.Wait()

	fileInfo, err := successFile.Stat()
	if err != nil {
		fmt.Println("Failed to get file information:", err)
		return
	}

	fmt.Printf("Successfully saved to the JSON file. File Size: %d bytes\n", fileInfo.Size())
}

func clearScreen() {
	var command string
	if runtime.GOOS == "windows" {
		command = "cls"
	} else {
		command = "clear"
	}

	cmd := exec.Command(command)
	cmd.Stdout = os.Stdout
	cmd.Run()
}

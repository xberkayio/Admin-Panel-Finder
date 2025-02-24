import os, time, sys, platform, aiohttp, asyncio

async def clearscreen():
    system = platform.system()
    if system == "Windows":
        command = "cls"
    elif system == "Linux":
        command = "clear"
    else:
        command = "clear"
    os.system(command)

async def rainbowtext(text, delay=0.1):
    colors = [
        "\033[31m", "\033[33m", "\033[32m", "\033[36m", "\033[34m", "\033[35m", "\033[37m"
    ]

    for i in range(len(text)):
        char = text[i]
        color = colors[i % len(colors)]
        sys.stdout.write(color + char)
        sys.stdout.flush()
        await asyncio.sleep(delay)
    sys.stdout.write("\033[0m")
    sys.stdout.write("\n")

try:
    async def bannerprint(h):
        for c in h + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            await asyncio.sleep(0.01)  # Gecikme süresini azaltabilirsiniz
except KeyboardInterrupt:
    print("\n\033[90m [-] See You Again ^-^")

async def slowprint(f):
    for c in f + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        await asyncio.sleep(0.01)  # Gecikme süresini azaltabilirsiniz

list = (
    "admin.php", "admin1.php", "admin1.html", "admin2.php", "admin2.html", "yonetim.php", "yonetim.html",
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
    "webmaster_logs", "filemgmt", "management", "admmgmt", "adm_mgmt", "exp", "expl", "exploit", "exploits", "acp"
)


async def main():
    await clearscreen()
    await rainbowtext("Coding by berkay")
    await bannerprint('''\033[92m
   _____       .___      .__               
  /  _  \    __| _/_____ |__| ____         
 /  /_\  \  / __ |/     \|  |/    \        
/    |    \/ /_/ |  Y Y  \  |   |  \       
\____|__  /\____ |__|_|  /__|___|  /       
        \/      \/     \/        \/        
     __________                      .__   
     \______   \_____    ____   ____ |  |  
      |     ___/\__  \  /    \_/ __ \|  |  
      |    |     / __ \|   |  \  ___/|  |__
      |____|    (____  /___|  /\___  >____/
                     \/     \/     \/         
\033[0m
''')
    print("\033[31m[!] Dont Abuse")
    print("\033[95mYou must to type http:// or https://")
    print(" \033[95mYou must add / at the end")
    url = input("\n\033[94mEnter the target url: ")
    input("\n\033[91mAttack strategy is ready. Enter to contiune or ctrl+c to exit")

    await slowprint('''\n \033[91mDo you feel the presence of blood flowing in your veins???''')
    await asyncio.sleep(2)

    async with aiohttp.ClientSession() as session:
        for keywords in list:
            target_url = url + keywords

            headers = {'user-agent': 'Mozilla/4.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/11.0.1245.0 Safari/537.36'}
            async with session.get(target_url, headers=headers) as response:
                if response.status == 200:
                    await clearscreen()
                    await rainbowtext("Coding by berkay")
                    await bannerprint('''\033[92m
   _____       .___      .__               
  /  _  \    __| _/_____ |__| ____         
 /  /_\  \  / __ |/     \|  |/    \        
/    |    \/ /_/ |  Y Y  \  |   |  \       
\____|__  /\____ |__|_|  /__|___|  /       
        \/      \/     \/        \/        
     __________                      .__   
     \______   \_____    ____   ____ |  |  
      |     ___/\__  \  /    \_/ __ \|  |  
      |    |     / __ \|   |  \  ___/|  |__
      |____|    (____  /___|  /\___  >____/
                     \/     \/     \/         
\033[0m
''')
                    print("\n\033[1;33m-------------------------------")
                    print("Admin panel Found ::: " + target_url)
                    print("-------------------------------\033[0m")
                    print("\n\033[90m [-] See You Again ^-^ ")
                    sys.exit()
                else:
                    print("\033[1;31m[-] Not Found ::: " + target_url)
                    await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())
import os

def getCommand(name: str, command: str):
    try:
        if len(os.environ[name]) == 0:
            raise KeyError
        return os.environ[name]
    except KeyError:
        return command
class _BotCommands:
    def __init__(self):
        self.StartCommand = getCommand('START_COMMAND', 'starts')
        self.MirrorCommand = getCommand('MIRROR_COMMAND', 'mirrors')
        self.UnzipMirrorCommand = getCommand('UNZIPMIRROR_COMMAND', 'unzipmirror')
        self.TarMirrorCommand = getCommand('TARMIRROR_COMMAND', 'tarmirror')
        self.ZipMirrorCommand = getCommand('ZIPMIRROR_COMMAND', 'zipmirror')
        self.QbMirrorCommand = getCommand('QBMIRROR_COMMAND', 'qbmirrors')
        self.QbUnzipMirrorCommand = getCommand('QBUNZIPMIRROR_COMMAND', 'qbunzipmirrors')
        self.QbTarMirrorCommand = getCommand('QBTARMIRROR_COMMAND', 'qbtarmirrors')
        self.QbZipMirrorCommand = getCommand('QBZIPMIRROR_COMMAND', 'qbzipmirrors')
        self.LeechSetCommand = getCommand('LEECHSET_COMMAND', 'leechsets')
        self.SetThumbCommand = getCommand('SETTHUMB_COMMAND', 'setthumbs')
        self.LeechCommand = getCommand('LEECH_COMMAND', 'leechs')
        self.TarLeechCommand = getCommand('TARLEECH_COMMAND', 'tarleechs')
        self.UnzipLeechCommand = getCommand('UNZIPLEECH_COMMAND', 'unzipleechs')
        self.ZipLeechCommand = getCommand('ZIPLEECH_COMMAND', 'zipleechs')
        self.QbLeechCommand = getCommand('QBLEECH_COMMAND', 'qbleechs')
        self.QbTarLeechCommand = getCommand('QBTARLEECH_COMMAND', 'qbtarleechs')
        self.QbUnzipLeechCommand = getCommand('QBUNZIPLEECH_COMMAND', 'qbunzipleech')
        self.QbZipLeechCommand = getCommand('QBZIPLEECH_COMMAND', 'qbzipleech')
        self.LeechWatchCommand = getCommand('LEECHWATCH_COMMAND', 'leechwatch')
        self.LeechTarWatchCommand = getCommand('LEECHTARWATCH_COMMAND', 'leechtarwatch')
        self.LeechZipWatchCommand = getCommand('LEECHZIPWATCH_COMMAND', 'leechzipwatch')
        self.CancelMirror = getCommand('CANCELMIRROR_COMMAND', 'cancels')
        self.CancelAllCommand = getCommand('CANCELALL_COMMAND', 'cancelalls')
        self.ListCommand = getCommand('LIST_COMMAND', 'searchs')
        self.StatusCommand = getCommand('STATUS_COMMAND', 'statuss')
        self.AuthorizedUsersCommand = getCommand('AUTHORIZEDUSERS_COMMAND', 'allusers')
        self.AuthorizeCommand = getCommand('AUTHORIZE_COMMAND', 'auths')
        self.UnAuthorizeCommand = getCommand('UNAUTHORIZE_COMMAND', 'unauths')
        self.AddSudoCommand = getCommand('ADDSUDO_COMMAND', 'addsudos')
        self.RmSudoCommand = getCommand('RMSUDO_COMMAND', 'rmsudos')
        self.PingCommand = getCommand('PING_COMMAND', 'pings')
        self.RestartCommand = getCommand('RESTART_COMMAND', 'restarts')
        self.StatsCommand = getCommand('STATS_COMMAND', 'statss')
        self.HelpCommand = getCommand('HELP_COMMAND', 'helps')
        self.LogCommand = getCommand('LOG_COMMAND', 'logs')
        self.SpeedCommand = getCommand('SPEED_COMMAND', 'speedtests')
        self.CloneCommand = getCommand('CLONE_COMMAND', 'clones')
        self.CountCommand = getCommand('COUNT_COMMAND', 'counts')
        self.WatchCommand = getCommand('WATCH_COMMAND', 'watchs')
        self.TarWatchCommand = getCommand('TARWATCH_COMMAND', 'tarwatchs')
        self.ZipWatchCommand = getCommand('ZIPWATCH_COMMAND', 'zipwatches')
        self.DeleteCommand = getCommand('DELETE_COMMAND', 'dels')
        self.ShellCommand = getCommand('SHELL_COMMAND', 'shells')
        self.ExecHelpCommand = getCommand('EXECHELP_COMMAND', 'exechelps')
        self.TsHelpCommand = getCommand('TSHELP_COMMAND', 'tshelps')

BotCommands = _BotCommands()

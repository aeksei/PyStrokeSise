from pyrow import pyrow
from pyrow.csafe import csafe_dic

is_debug = False


class PyErgRace(pyrow.PyErg):
    """
    Manages low-level erg communication for race
    """
    _serial_num = None
    _erg_num = 0xFD
    _race_line = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if is_debug:
            import logging
            self.raw_logger.setLevel(logging.DEBUG)

            console = logging.StreamHandler()
            console.setLevel(logging.DEBUG)
            self.raw_logger.addHandler(console)

    def reset_erg_num(self):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_reset_erg_num
        :return:
        """
        csafe_cmd = 'CSAFE_GETPMCFG_CMD'
        cmd = 'reset_erg_num'
        self.raw_logger.debug('Erg {:02X} {}'.format(self._erg_num, cmd))

        data = csafe_dic.cmds[cmd]
        message = [[0xFF, 0x00, csafe_cmd, len(data)]]
        message.extend(data)

        self.send(message)

    def get_serial_num(self, destination=0xFD):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_get_serial_num
        :return: serial number of erg [0xFF, 0xFF, 0xFF, 0xFF]
        """
        data = csafe_dic.cmds['get_serial_num']
        message = [[destination, 0x00, 'CSAFE_GETPMCFG_CMD', len(data)]]
        message.extend(data)
        # TODO return format
        return self.send(message)

    def set_erg_num(self, serial_num, erg_num):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_set_erg_num
        :return:
        """

        data = csafe_dic.cmds['set_erg_num'][:-1]
        data.extend(serial_num)
        data.append(erg_num)

        destination = 0xFD if erg_num is 0x01 else 0xFF
        message = [[destination, 0x00, 'CSAFE_SETPMCFG_CMD', len(data)]]
        message.extend(data)

        self.send(message)

    def set_erg_num_check(self, destination, serial_num):
        """
        get_erg_num_confirm
        :param destination:
        :param serial_num:
        :return: confirm set erg num
        """

        data = csafe_dic.cmds['get_erg_num_confirm'][:-1]
        data.extend(serial_num)

        message = [[destination, 0x00, 'CSAFE_GETPMCFG_CMD', len(data)]]
        message.extend(data)

        self.send(message)

    def set_screen_state(self, destination, state):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_set_screen_state@@YAFGEE@Z(guessed Arg1,Arg2,Arg3)

        :return:
        """
        data = csafe_dic.cmds['set_screen_state'][:-1]
        data.append(state)

        message = [[destination, 0x00, 'CSAFE_SETPMCFG_CMD', len(data)]]
        message.extend(data)

        self.send(message)

    def close(self):
        raw_command = "02 f0 01 00 76 04 13 02 02 06 67 f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=csafe_command["destination"],
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

        raw_command = "02 f0 01 00 76 03 1e 01 06 6c f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=csafe_command["destination"],
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

        raw_command = "02 f0 01 00 76 04 13 02 02 15 74 f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=csafe_command["destination"],
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

        raw_command = "02 f0 01 00 76 03 1e 01 00 6a f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=csafe_command["destination"],
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def VRPM3Race_100012D0(self, destination=0x01):
        """
        VRPM3Race.100012D0(guessed Arg1,Arg2)
        :return:
        """
        raw_command = "02 f0 01 00 7e 01 80 ff f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def call_10001210(self, destination=0x01):
        raw_command = "02 f0 01 00 7e 01 9a e5 f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def VRPM3Race_10001380(self, destination=0x01):  # get serial num
        """
        VRPM3Race.10001380(guessed Arg1,Arg2)
        :return:
        """
        raw_command = "02 f0 01 00 7e 01 82 fd f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def call_10001400(self, destination=0x01):
        raw_command = "02 f0 01 00 76 0e 1a 0c 19 a6 84 88 67 6f 21 cc 19 8c 48 e6 03 f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def VRPM3Race_10001000(self, destination=0x01):
        """
        setting erg
        :return:
        """

        self.VRPM3Race_100012D0(destination=destination)
        self.call_10001210(destination=destination)
        self.VRPM3Race_10001380(destination=destination)  # get serial num
        self.call_10001400(destination=destination)

    def set_race_idle_params(self, destination=0x01):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_set_race_idle_params@@YAFGGGGG@Z
        :return:
        """
        raw_command = "02 f0 01 00 76 0a 21 08 ff ff 38 40 00 05 00 01 29 f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def set_datetime(self, destination=0x01):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_set_datetime@@YAFGEEEEEG@Z>]
        :return:
        """
        raw_command = "02 f0 01 00 76 09 22 07 0a 0e 01 0c 01 07 e2 b7 f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def set_screen_error_mode(self):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_set_screen_error_mode@@YAFGE@Z>]
        :return:
        """
        raw_command = "02 F0 01 00 76 03 27 01 00 53 F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=csafe_command["destination"],
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def set_cpu_tick_rate(self, destination=0x01, bar=0x01):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_set_cpu_tick_rate@@YAFGE@Z
        :return:
        """
        raw_command = "02 f0 01 00 76 03 25 01 " + hex(bar)[2:] + " 50 f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def get_cpu_tick_rate(self, destination=0x01):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_get_cpu_tick_rate@@YAFGPAE@Z
        :return:
        """
        raw_command = "02 f0 01 00 7e 01 9d e2 f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        resp = self.send(message=message,
                         destination=destination,
                         source=csafe_command["source"],
                         count_bytes=csafe_command["data_byte_command"])

        return resp

    def get_erg_info(self, destination=0x01):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_get_erg_info@@YAFGPAKPAE1111111111PAG@Z(guessed Arg1,Arg2,Arg3,Arg4,Arg5,Arg6,Arg7,Arg8,Arg9,Arg10,Arg11,Arg12,Arg13,Arg14)
        """
        raw_command = "02 f0 01 00 7e 02 98 c9 2d f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def set_race_starting_physical_address(self, destionation=0x01):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_set_race_starting_physical_address@@YAFGE@Z
        :return:
        """
        raw_command = "02 f0 01 00 76 03 2c 01 01 59 f2"

        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destionation,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def set_race_operation_type(self, destination=0x01, state=0x04):
        """
        VRPM3Csafe.?tkcmdsetCSAFE_set_race_operation_type@@YAFGE@Z
        :return:
        """
        # raw_command = "02 f0 01 00 76 03 1e 01 04 6e f2"
        raw_command = "02 f0 01 00 76 03 1e 01 " + str(hex(state)[2:]) + " 6e f2"

        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def get_race_lane_request(self):
        """
        1000A2B7
        VRPM3Csafe.?tkcmdsetCSAFE_get_race_lane_request@@YAFGPAE@Z
        :return:
        """
        raw_command = "02 f0 ff 00 7e 04 51 02 00 ff d6 f2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        return self.send(message=message,
                         destination=csafe_command["destination"],
                         source=csafe_command["source"],
                         count_bytes=csafe_command["data_byte_command"])

    def set_race_lane_setup(self, destination=0x01, race_line=0x01):
        """
        1000A317
        VRPM3Csafe.?tkcmdsetCSAFE_set_race_lane_setup@@YAFGGG@Z
        :return:
        """
        raw_command = "02 F0 01 00 7E 04 0B 02 " + str(race_line) + " 00 72 F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def foo(self, destination=0x01):
        raw_command = "02 F0 01 00 7E 01 87 F8 F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def erg_enumeration_check(self, destination=0x01):
        """
        10015127
        VRPM3Race.erg_enumeration_check

        :return:
        """
        raw_command = "02 F0 01 00 7E 01 87 F8 F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

        self.get_serial_num(destination=destination)

    def set_workout_type(self, destination=0x01):
        """
        00BBC668
        VRPM3Csafe.?tkcmdsetCSAFE_set_workout_type@@YAFGE@Z

        :return:
        """
        raw_command = "02 F0 01 00 76 03 01 01 01 74 F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def set_race_participant(self, name, lane=0x00, destination=0xFF):
        """
        00BBB81F
        VRPM3Csafe.?tkcmdsetCSAFE_set_race_participant@@YAFGGPAD@Z

        :return:
        """
        # raw_command = "02 F0 FF 00 76 09 32 07 02 4C 61 6E 65 32 00 5C F2"  # Lane2 4C 61 6E 65 32
        message = [hex(ord(c))[2:] for c in name]
        message.append(hex(0)[2:])
        message.insert(0, hex(lane)[2:])  # add number lane
        message.insert(0, hex(len(message))[2:])  # add length sub message
        message.insert(0, hex(50)[2:])  # add id command
        message.insert(0, hex(len(message))[2:])  # add length message
        # message = [50, len(name) + 2, lane] + name + [0]  # 32 0A 00 + name + 00

        raw_command = "02 F0 FF 00 76 " + " ".join(message) + " 5C F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def get_race_participant_count(self, destination=0x01):
        """
        00BBBD0F
        VRPM3Csafe.?tkcmdsetCSAFE_get_race_participant_count@@YAFGPAE@Z

        :return:
        """
        raw_command = "02 F0 02 00 7E 01 96 E9 F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])

        resp = self.send(message=message,
                         destination=destination,
                         source=csafe_command["source"],
                         count_bytes=csafe_command["data_byte_command"])
        return resp

    def get_tick_timebase(self, destination=0x01):
        """
        1000B635
        VRPM3Csafe.?tkcmdsetCSAFE_get_tick_timebase@@YAFGPAM@Z

        :return:
        """
        raw_command = "02 F0 01 00 7E 01 83 FC F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def latch_tick_time(self, destination=0x01):
        """
        1000CD4F
        VRPM3Csafe.?tkcmdsetCSAFE_latch_tick_time@@YAFG@Z

        :return:
        """
        raw_command = "02 F0 01 00 77 01 D7 A1 F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def get_latched_tick_time(self, destination=0x01):
        """
        1000CDC6
        VRPM3Csafe.?tkcmdsetCSAFE_get_latched_tick_time@@YAFGPAM@Z

        """
        raw_command = "02 F0 01 00 7E 01 C4 BB F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def set_race_start_params(self, destination=0x01):
        """
        1000CFD5
        VRPM3Csafe.?tkcmdsetCSAFE_set_race_start_params@@YAFGEEKKK@Z

        :return:
        """
        raw_command = "02 F0 01 00 76 10 0D 0E 00 00 00 00 42 A8 00 00 44 9B 00 00 46 78 6E F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def update_race_data(self, destination=0x01):
        """
        1000DF53
        VRPM3Csafe.?tkcmdsetCSAFE_update_race_data@@YAFGPAUTKCMDSET_PM3_RACE_DATA@@PAUTKCMDSET_OVERALL_RACE_DATA@@@Z

        :return:
        """
        raw_command = "02 F0 02 00 76 22 33 1D 00 01 00 00 00 00 00 00 00 00 00 00 02 01 00 00 00 00 01 02 00 00 00 00 00 00 00 00 00 C6 BA BC BB F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def set_all_race_params(self, destination=0x01, distance=2000):
        """
        1000C8B1
        VRPM3Csafe.?tkcmdsetCSAFE_set_all_race_params@@YAFGKKKEEKKE@Z

        :return:
        """
        distance = " ".join(to_hex.int_to_hex(4, distance))
        raw_command = "02 F0 01 00 1D 04 00 00 00 80 1F 04 00 00 02 00 20 04 00 00 0F 00 01 01 03 03 05 80 " \
                      + distance + " 05 05 80 00 00 01 F4 09 01 00 D4 F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])

    def configure_workout(self, destination=0x01):
        """
        1000C8E1
        VRPM3Csafe.?tkcmdsetCSAFE_configure_workout@@YAFGE@Z

        :return:
        """
        raw_command = "02 F0 01 00 76 03 14 01 01 61 F2"
        csafe_command = to_hex.prerare_raw_command(raw_command)
        message = [csafe_command["id"]]
        message.extend(csafe_command["data"])
        self.send(message=message,
                  destination=destination,
                  source=csafe_command["source"],
                  count_bytes=csafe_command["data_byte_command"])
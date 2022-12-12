
import psutil
from platform import uname


def correct_size(bts, ending='iB'):
    """
    Метод предназначен для конвертации данных: Биты в различные системы
    :param bts:
    :param ending:
    :return: None
    """
    size = 1024
    for item in ["", "K", "M", "G", "T", "P"]:
        if bts < size:
            return f"{bts:.2f}{item}{ending}"
        bts /= size


def creating_file():
    """
    метод предназначен для забора информации о системе
    :return: None
    """
    system = {'comp_name': uname().node,
               'os_name': f"{uname().system} {uname().release}",
                'version': uname().version,
                'machine': uname().machine
              }
    cpu = {
        'name': uname().processor,
        'phisycal_core': psutil.cpu_count(logical=False),
        'all_core': psutil.cpu_count(logical=True),
        'freq_max': f"{psutil.cpu_freq().max:.2f}Мгц"
    }
    ram = {
        'volume': correct_size(psutil.virtual_memory().total),
        'aviable': correct_size(psutil.virtual_memory().available),
        'used': correct_size(psutil.virtual_memory().used)
    }
    for partition in psutil.disk_partitions():
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        disk = {
            'file_system': partition.fstype,
            'size_total': correct_size(
                partition_usage.total),
            'size_used': correct_size(
                partition_usage.used),
            'size_free': correct_size(
                partition_usage.free),
            'percent':
                f'{partition_usage.percent}'
        }
    return system, cpu, ram, disk



def main():
        dict_info = creating_file()
        file_name = dict_info[0]['comp_name']
        cnt = 0
        with open(str(file_name)+'.txt', 'w') as f:
            for i in dict_info:
                if cnt == 0:
                    f.write('INFO ABOUT SYSTEM'+'\n')
                elif cnt == 1:
                    f.write('INFO ABOUT CPU' + '\n')
                elif cnt == 2:
                    f.write('INFO ABOUT RAM' + '\n')
                elif cnt == 3:
                    f.write('INFO ABOUT DISK' + '\n')
                for key, value in i.items():
                    f.write(str(key) + ':' + str(value)+'\n')
                f.write('\n')
                cnt+=1
        f.close()

if __name__ == "__main__":
    main()

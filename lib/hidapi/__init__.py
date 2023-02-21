## 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""Generic Human Interface Device API."""

import platform as _platform

if _platform.system() in ('Darwin', 'Windows'):
    from hidapi.hidapi import close  # noqa: F401
    from hidapi.hidapi import enumerate  # noqa: F401
    from hidapi.hidapi import find_paired_node  # noqa: F401
    from hidapi.hidapi import find_paired_node_wpid  # noqa: F401
    from hidapi.hidapi import get_manufacturer  # noqa: F401
    from hidapi.hidapi import get_product  # noqa: F401
    from hidapi.hidapi import get_serial  # noqa: F401
    from hidapi.hidapi import monitor_glib  # noqa: F401
    from hidapi.hidapi import open  # noqa: F401
    from hidapi.hidapi import open_path  # noqa: F401
    from hidapi.hidapi import read  # noqa: F401
    from hidapi.hidapi import write  # noqa: F401
else:
    from hidapi.udev import close  # noqa: F401
    from hidapi.udev import enumerate  # noqa: F401
    from hidapi.udev import find_paired_node  # noqa: F401
    from hidapi.udev import find_paired_node_wpid  # noqa: F401
    from hidapi.udev import get_manufacturer  # noqa: F401
    from hidapi.udev import get_product  # noqa: F401
    from hidapi.udev import get_serial  # noqa: F401
    from hidapi.udev import monitor_glib  # noqa: F401
    from hidapi.udev import open  # noqa: F401
    from hidapi.udev import open_path  # noqa: F401
    from hidapi.udev import read  # noqa: F401
    from hidapi.udev import write  # noqa: F401

__version__ = '0.9'
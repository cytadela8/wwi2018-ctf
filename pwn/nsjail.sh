#!/bin/bash
mkdir /sys/fs/cgroup/{cpu,memory,pids}/NSJAIL
nsjail                                \
    -Ml --port "${PORT-9000}"         \
    --user pwn --group pwn            \
    --cwd /app                        \
    -R /app -R /bin -R /lib -R /lib64 \
    --time_limit 60                   \
    --cgroup_cpu_ms_per_sec 100       \
    --cgroup_mem_max 16777216         \
    --cgroup_pids_max 32              \
    -- "$@"

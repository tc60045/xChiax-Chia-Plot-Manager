class Job:
    name = None
    current_work_id = 0

    farmer_public_key = None
    pool_public_key = None

    total_running = 0
    total_kicked_off = 0
    total_completed = 0
    max_concurrent = 0
    max_concurrent_with_start_early = 0
    max_plots = 0
    temporary2_destination_sync = None

    initial_delay_minutes = None
    stagger_minutes = None
    max_for_phase_1 = None
    concurrency_start_early_phase = None
    concurrency_start_early_phase_delay = None

    running_work = []

    temporary_directory = None
    temporary2_directory = None
    destination_directory = []               # this will be a symbolic link
    exclude_final_directory = None
    skip_full_destinations = None
    size = None
    bitfield = None
    threads = None
    buckets = None
    memory_buffer = None

    unix_process_priority = 10
    windows_process_priority = 32

    enable_cpu_affinity = False
    cpu_affinity = []


class Work:                                  # certain we will add more to this
    work_id = None
    job = None
    pid = None
    plot_id = None
    log_file = None
    plot_filename = None
    order_number = None    # I think we can add this to work...

    temporary_drive = None
    temporary2_drive = None
    destination_drive = None
    mount_assigned = None

    current_phase = 1

    datetime_start = None
    datetime_end = None
    copytime_start = None
    seed_start = None

    phase_times = {}
    total_run_time = None

    completed = False

    progress = 0
    temp_file_size = 0
    k_size = None


class Order:
    order_id = None
    farmer_public_key = None
    pool_public_key = None
    size = None


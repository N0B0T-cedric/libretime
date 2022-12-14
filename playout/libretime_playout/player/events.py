from enum import Enum


class EventKind(str, Enum):
    FILE = "file"
    EVENT = "event"
    STREAM_BUFFER_START = "stream_buffer_start"
    STREAM_OUTPUT_START = "stream_output_start"
    STREAM_BUFFER_END = "stream_buffer_end"
    STREAM_OUTPUT_END = "stream_output_end"

from __future__ import annotations

import asyncio
import datetime
import logging
from typing import (
    TYPE_CHECKING,
    Any,
    AsyncIterator,
    Callable,
    Coroutine,
    Dict,
    Generator,
    List,
    Literal,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

import aiohttp

from .user import User, ClientUser
from .invite import Invite
from .template import Template
from .widget import Widget
from .guild import Guild
from .emoji import Emoji
from .channel import _threaded_channel_factory, PartialMessageable
from .enums import ChannelType
from .mentions import AllowedMentions
from .errors import *
from .enums import Status
from .flags import ApplicationFlags, Intents
from .gateway import *
from .activity import ActivityTypes, BaseActivity, create_activity
from .voice_client import VoiceClient
from .http import HTTPClient
from .state import ConnectionState
from . import utils
from .utils import MISSING, time_snowflake
from .object import Object
from .backoff import ExponentialBackoff
from .webhook import Webhook
from .appinfo import AppInfo
from .ui.view import View
from .stage_instance import StageInstance
from .threads import Thread
from .sticker import GuildSticker, StandardSticker, StickerPack, _sticker_factory

if TYPE_CHECKING:
    from types import TracebackType

    from typing_extensions import Self

    from .abc import Messageable, PrivateChannel, Snowflake, SnowflakeTime
    from .app_commands import Command, ContextMenu
    from .automod import AutoModAction, AutoModRule
    from .channel import DMChannel, GroupChannel
    from .ext.commands import AutoShardedBot, Bot, Context, CommandError
    from .guild import GuildChannel
    from .integrations import Integration
    from .interactions import Interaction
    from .member import Member, VoiceState
    from .message import Message
    from .raw_models import (
        RawAppCommandPermissionsUpdateEvent,
        RawBulkMessageDeleteEvent,
        RawIntegrationDeleteEvent,
        RawMemberRemoveEvent,
        RawMessageDeleteEvent,
        RawMessageUpdateEvent,
        RawReactionActionEvent,
        RawReactionClearEmojiEvent,
        RawReactionClearEvent,
        RawThreadDeleteEvent,
        RawThreadMembersUpdate,
        RawThreadUpdateEvent,
        RawTypingEvent,
    )
    from .reaction import Reaction
    from .role import Role
    from .scheduled_event import ScheduledEvent
    from .threads import ThreadMember
    from .types.guild import Guild as GuildPayload
    from .voice_client import VoiceProtocol
    from .audit_logs import AuditLogEntry

class Client:
    def __init__(self, **options:Any) -> None:
        pass
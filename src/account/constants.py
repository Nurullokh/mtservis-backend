class UserStatus:
    ACTIVE = "active"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"

    choices = ((ACTIVE, ACTIVE), (BLOCKED, BLOCKED), (RESTRICTED, RESTRICTED))


class UserType:
    ADMIN = "admin"
    CONSUMER = "consumer"
    TECHNICIAN = "technician"

    choices = (
        (ADMIN, ADMIN),
        (CONSUMER, CONSUMER),
        (TECHNICIAN, TECHNICIAN),
    )


class Regions:
    ANDIJAN = "andijan"
    BUKHARA = "bukhara"
    DJIZZAK = "djizzak"
    FERGANA = "fergana"
    KASHKADARYA = "kashkadarya"
    KHOREZM = "khorezm"
    NAMANGAN = "namangan"
    NAVOI = "navoi"
    SAMARKAND = "samarkand"
    SURKHANDARYA = "surkhandarya"
    SRYDARYA = "syrdarya"
    TASHKENT_REGION = "tashkent_region"
    TASHKENT_CITY = "tashkent_city"
    KARAKALPAKISTAN = "karakalpakistan"

    choices = (
        (ANDIJAN, ANDIJAN),
        (BUKHARA, BUKHARA),
        (DJIZZAK, DJIZZAK),
        (FERGANA, FERGANA),
        (KASHKADARYA, KASHKADARYA),
        (KHOREZM, KHOREZM),
        (NAMANGAN, NAMANGAN),
        (NAVOI, NAVOI),
        (SAMARKAND, SAMARKAND),
        (SURKHANDARYA, SURKHANDARYA),
        (SRYDARYA, SRYDARYA),
        (TASHKENT_REGION, TASHKENT_REGION),
        (TASHKENT_CITY, TASHKENT_CITY),
        (KARAKALPAKISTAN, KARAKALPAKISTAN),
    )

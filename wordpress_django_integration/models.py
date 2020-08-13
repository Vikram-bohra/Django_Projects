# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class WpAhmAssets(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    path = models.TextField()
    owner = models.IntegerField()
    activities = models.TextField()
    comments = models.TextField()
    access = models.TextField()
    metadata = models.TextField()

    class Meta:
        managed = False
        db_table = 'wp_ahm_assets'


class WpAhmDownloadStats(models.Model):
    pid = models.IntegerField()
    uid = models.IntegerField()
    oid = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    timestamp = models.IntegerField()
    ip = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_ahm_download_stats'


class WpAhmEmails(models.Model):
    email = models.CharField(max_length=255)
    pid = models.IntegerField()
    date = models.IntegerField()
    custom_data = models.TextField()
    request_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_ahm_emails'


class WpCommentmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    comment_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_commentmeta'


class WpComments(models.Model):
    comment_id = models.BigAutoField(db_column='comment_ID', primary_key=True)  # Field name made lowercase.
    comment_post_id = models.BigIntegerField(db_column='comment_post_ID')  # Field name made lowercase.
    comment_author = models.TextField()
    comment_author_email = models.CharField(max_length=100)
    comment_author_url = models.CharField(max_length=200)
    comment_author_ip = models.CharField(db_column='comment_author_IP', max_length=100)  # Field name made lowercase.
    comment_date = models.DateTimeField()
    comment_date_gmt = models.DateTimeField()
    comment_content = models.TextField()
    comment_karma = models.IntegerField()
    comment_approved = models.CharField(max_length=20)
    comment_agent = models.CharField(max_length=255)
    comment_type = models.CharField(max_length=20)
    comment_parent = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_comments'


class WpFmLog(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    operation_id = models.CharField(max_length=32)
    file_path = models.CharField(max_length=1024)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'wp_fm_log'


class WpLinks(models.Model):
    link_id = models.BigAutoField(primary_key=True)
    link_url = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_image = models.CharField(max_length=255)
    link_target = models.CharField(max_length=25)
    link_description = models.CharField(max_length=255)
    link_visible = models.CharField(max_length=20)
    link_owner = models.BigIntegerField()
    link_rating = models.IntegerField()
    link_updated = models.DateTimeField()
    link_rel = models.CharField(max_length=255)
    link_notes = models.TextField()
    link_rss = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_links'


class WpLoginizerLogs(models.Model):
    username = models.CharField(max_length=255)
    time = models.IntegerField()
    count = models.IntegerField()
    lockout = models.IntegerField()
    ip = models.CharField(unique=True, max_length=255)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wp_loginizer_logs'


class WpOdbLogs(models.Model):
    odb_id = models.AutoField(primary_key=True)
    odb_timestamp = models.CharField(max_length=20)
    odb_revisions = models.IntegerField()
    odb_trash = models.IntegerField()
    odb_spam = models.IntegerField()
    odb_tags = models.IntegerField()
    odb_transients = models.IntegerField()
    odb_pingbacks = models.IntegerField()
    odb_oembeds = models.IntegerField()
    odb_orphans = models.IntegerField()
    odb_tables = models.IntegerField()
    odb_before = models.CharField(max_length=20)
    odb_after = models.CharField(max_length=20)
    odb_savings = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_odb_logs'


class WpOptions(models.Model):
    option_id = models.BigAutoField(primary_key=True)
    option_name = models.CharField(unique=True, max_length=191)
    option_value = models.TextField()
    autoload = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'wp_options'


class WpPostmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    post_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_postmeta'


class WpPosts(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    post_author = models.BigIntegerField()
    post_date = models.DateTimeField()
    post_date_gmt = models.DateTimeField()
    post_content = models.TextField()
    post_title = models.TextField()
    post_excerpt = models.TextField()
    post_status = models.CharField(max_length=20)
    comment_status = models.CharField(max_length=20)
    ping_status = models.CharField(max_length=20)
    post_password = models.CharField(max_length=255)
    post_name = models.CharField(max_length=200)
    to_ping = models.TextField()
    pinged = models.TextField()
    post_modified = models.DateTimeField()
    post_modified_gmt = models.DateTimeField()
    post_content_filtered = models.TextField()
    post_parent = models.BigIntegerField()
    guid = models.CharField(max_length=255)
    menu_order = models.IntegerField()
    post_type = models.CharField(max_length=20)
    post_mime_type = models.CharField(max_length=100)
    comment_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_posts'


class WpTermRelationships(models.Model):
    object_id = models.BigIntegerField(primary_key=True)
    term_taxonomy_id = models.BigIntegerField()
    term_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_relationships'
        unique_together = (('object_id', 'term_taxonomy_id'),)


class WpTermTaxonomy(models.Model):
    term_taxonomy_id = models.BigAutoField(primary_key=True)
    term_id = models.BigIntegerField()
    taxonomy = models.CharField(max_length=32)
    description = models.TextField()
    parent = models.BigIntegerField()
    count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_term_taxonomy'
        unique_together = (('term_id', 'taxonomy'),)


class WpTermmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    term_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_termmeta'


class WpTerms(models.Model):
    term_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    term_group = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_terms'


class WpUsermeta(models.Model):
    umeta_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_usermeta'


class WpUsers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_login = models.CharField(max_length=60)
    user_pass = models.CharField(max_length=255)
    user_nicename = models.CharField(max_length=50)
    user_email = models.CharField(max_length=100)
    user_url = models.CharField(max_length=100)
    user_registered = models.DateTimeField()
    user_activation_key = models.CharField(max_length=255)
    user_status = models.IntegerField()
    display_name = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'wp_users'


class WpWcDownloadLog(models.Model):
    download_log_id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    permission_id = models.BigIntegerField()
    user_id = models.BigIntegerField(blank=True, null=True)
    user_ip_address = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_download_log'


class WpWcProductMetaLookup(models.Model):
    product_id = models.BigIntegerField(primary_key=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    virtual = models.IntegerField(blank=True, null=True)
    downloadable = models.IntegerField(blank=True, null=True)
    min_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    onsale = models.IntegerField(blank=True, null=True)
    stock_quantity = models.FloatField(blank=True, null=True)
    stock_status = models.CharField(max_length=100, blank=True, null=True)
    rating_count = models.BigIntegerField(blank=True, null=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    total_sales = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wc_product_meta_lookup'


class WpWcWebhooks(models.Model):
    webhook_id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=200)
    name = models.TextField()
    user_id = models.BigIntegerField()
    delivery_url = models.TextField()
    secret = models.TextField()
    topic = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_created_gmt = models.DateTimeField()
    date_modified = models.DateTimeField()
    date_modified_gmt = models.DateTimeField()
    api_version = models.SmallIntegerField()
    failure_count = models.SmallIntegerField()
    pending_delivery = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wc_webhooks'


class WpWoocommerceApiKeys(models.Model):
    key_id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    description = models.CharField(max_length=200, blank=True, null=True)
    permissions = models.CharField(max_length=10)
    consumer_key = models.CharField(max_length=64)
    consumer_secret = models.CharField(max_length=43)
    nonces = models.TextField(blank=True, null=True)
    truncated_key = models.CharField(max_length=7)
    last_access = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_api_keys'


class WpWoocommerceAttributeTaxonomies(models.Model):
    attribute_id = models.BigAutoField(primary_key=True)
    attribute_name = models.CharField(max_length=200)
    attribute_label = models.CharField(max_length=200, blank=True, null=True)
    attribute_type = models.CharField(max_length=20)
    attribute_orderby = models.CharField(max_length=20)
    attribute_public = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_attribute_taxonomies'


class WpWoocommerceDownloadableProductPermissions(models.Model):
    permission_id = models.BigAutoField(primary_key=True)
    download_id = models.CharField(max_length=36)
    product_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    order_key = models.CharField(max_length=200)
    user_email = models.CharField(max_length=200)
    user_id = models.BigIntegerField(blank=True, null=True)
    downloads_remaining = models.CharField(max_length=9, blank=True, null=True)
    access_granted = models.DateTimeField()
    access_expires = models.DateTimeField(blank=True, null=True)
    download_count = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_downloadable_product_permissions'


class WpWoocommerceLog(models.Model):
    log_id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    level = models.SmallIntegerField()
    source = models.CharField(max_length=200)
    message = models.TextField()
    context = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_log'


class WpWoocommerceOrderItemmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    order_item_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_order_itemmeta'


class WpWoocommerceOrderItems(models.Model):
    order_item_id = models.BigAutoField(primary_key=True)
    order_item_name = models.TextField()
    order_item_type = models.CharField(max_length=200)
    order_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_order_items'


class WpWoocommercePaymentTokenmeta(models.Model):
    meta_id = models.BigAutoField(primary_key=True)
    payment_token_id = models.BigIntegerField()
    meta_key = models.CharField(max_length=255, blank=True, null=True)
    meta_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_payment_tokenmeta'


class WpWoocommercePaymentTokens(models.Model):
    token_id = models.BigAutoField(primary_key=True)
    gateway_id = models.CharField(max_length=200)
    token = models.TextField()
    user_id = models.BigIntegerField()
    type = models.CharField(max_length=200)
    is_default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_payment_tokens'


class WpWoocommerceSessions(models.Model):
    session_id = models.BigAutoField(primary_key=True)
    session_key = models.CharField(unique=True, max_length=32)
    session_value = models.TextField()
    session_expiry = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_sessions'


class WpWoocommerceShippingZoneLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    zone_id = models.BigIntegerField()
    location_code = models.CharField(max_length=200)
    location_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zone_locations'


class WpWoocommerceShippingZoneMethods(models.Model):
    zone_id = models.BigIntegerField()
    instance_id = models.BigAutoField(primary_key=True)
    method_id = models.CharField(max_length=200)
    method_order = models.BigIntegerField()
    is_enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zone_methods'


class WpWoocommerceShippingZones(models.Model):
    zone_id = models.BigAutoField(primary_key=True)
    zone_name = models.CharField(max_length=200)
    zone_order = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_shipping_zones'


class WpWoocommerceTaxRateLocations(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    location_code = models.CharField(max_length=200)
    tax_rate_id = models.BigIntegerField()
    location_type = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_tax_rate_locations'


class WpWoocommerceTaxRates(models.Model):
    tax_rate_id = models.BigAutoField(primary_key=True)
    tax_rate_country = models.CharField(max_length=2)
    tax_rate_state = models.CharField(max_length=200)
    tax_rate = models.CharField(max_length=8)
    tax_rate_name = models.CharField(max_length=200)
    tax_rate_priority = models.BigIntegerField()
    tax_rate_compound = models.IntegerField()
    tax_rate_shipping = models.IntegerField()
    tax_rate_order = models.BigIntegerField()
    tax_rate_class = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'wp_woocommerce_tax_rates'


class WpWpdevartGallery(models.Model):
    id = models.BigAutoField(unique=True)
    time = models.DateTimeField()
    gallery = models.TextField(blank=True, null=True)
    album = models.TextField(blank=True, null=True)
    image_description = models.TextField(blank=True, null=True)
    image_name = models.TextField(blank=True, null=True)
    order_id = models.BigIntegerField()
    img_id = models.BigIntegerField()
    published = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wpdevart_gallery'


class WpWpdevartGalleryPopupTheme(models.Model):
    id = models.AutoField(unique=True)
    name = models.CharField(max_length=512)
    option_value = models.TextField()
    default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wpdevart_gallery_popup_theme'


class WpWpdevartGalleryTheme(models.Model):
    id = models.AutoField(unique=True)
    name = models.CharField(max_length=512)
    option_value = models.TextField()
    default = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wp_wpdevart_gallery_theme'


class WpWpdevartImages(models.Model):
    id = models.BigAutoField(unique=True)
    image_h = models.TextField(blank=True, null=True)
    image_w = models.TextField(blank=True, null=True)
    image_size = models.TextField(blank=True, null=True)
    image_type = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=4048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wpdevart_images'


class WpWpfmBackup(models.Model):
    backup_name = models.TextField(blank=True, null=True)
    backup_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wp_wpfm_backup'

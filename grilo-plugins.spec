%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1

%define api	0.3

Summary:	Plugins for the Grilo framework
Name:		grilo-plugins
Version:	0.3.7
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		https://live.gnome.org/Grilo
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(avahi-gobject)
BuildRequires:	pkgconfig(avahi-glib)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmime-3.0)
BuildRequires:	pkgconfig(gom-1.0)
BuildRequires:	pkgconfig(gupnp-1.0)
BuildRequires:	pkgconfig(gupnp-av-1.0)
BuildRequires:	pkgconfig(libdmapsharing-3.0)
BuildRequires:	pkgconfig(libgdata)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libmediaart-2.0)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(rest-0.7)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(tracker-sparql-2.0)
BuildRequires:	pkgconfig(grilo-0.3)
BuildRequires:	pkgconfig(totem-plparser)
BuildRequires:	pkgconfig(gom-1.0)
Requires:	grilo >= 0.2.6

%description
Grilo is a framework that provides access to different sources of
multimedia content, using a pluggable system.
This package contains plugins to get information from theses sources:
- Apple Trailers
- Bookmarks
- Filesystem
- Flickr
- Gravatar
- Jamendo
- Last.fm (for album arts)
- Local metadata (album arts and thumbnails)
- Metadata Store
- Podcasts
- Shoutcast
- Tracker
- UPnP
- Vimeo
- Youtube

%prep
%setup -q
%apply_patches

%build
%configure \
	--disable-static \
	--disable-shoutcast \
	--disable-bookmarks \
	--enable-filesystem \
	--enable-flickr	\
	--enable-gravatar \
	--enable-jamendo \
	--enable-lastfm-albumart \
	--enable-localmetadata \
	--enable-metadata-store \
	--enable-podcasts \
	--enable-shoutcast \
	--enable-tracker \
	--enable-vimeo \
	--enable-youtube \
	--enable-compile-warnings=no

%make

%install
%makeinstall_std

%find_lang %{name}

# Remove files that will not be packaged
find %{buildroot} -name "*.la" -delete
# md - not sure what do with these help files
rm -fr %{buildroot}/%{_datadir}/gnome
rm %{buildroot}%{_datadir}/help/C/examples/example-tmdb.c

%files -f %{name}.lang
%doc AUTHORS NEWS README
#{_libdir}/grilo-%{api}/grl-bookmarks.xml
#{_libdir}/grilo-%{api}/libgrlbookmarks.so

#{_libdir}/grilo-%{api}/grl-dleyna.xml
%{_libdir}/grilo-%{api}/libgrldleyna.so

#{_libdir}/grilo-%{api}/grl-filesystem.xml
%{_libdir}/grilo-%{api}/libgrlfilesystem.so

#{_libdir}/grilo-%{api}/grl-flickr.xml
%{_libdir}/grilo-%{api}/libgrlflickr.so

#{_libdir}/grilo-%{api}/grl-gravatar.xml
%{_libdir}/grilo-%{api}/libgrlgravatar.so

#{_libdir}/grilo-%{api}/grl-jamendo.xml
%{_libdir}/grilo-%{api}/libgrljamendo.so

#{_libdir}/grilo-%{api}/grl-lastfm-albumart.xml
#{_libdir}/grilo-%{api}/libgrllastfm-albumart.so

#{_libdir}/grilo-%{api}/grl-local-metadata.xml
%{_libdir}/grilo-%{api}/libgrllocalmetadata.so

#{_libdir}/grilo-%{api}/grl-magnatune.xml
%{_libdir}/grilo-%{api}/libgrlmagnatune.so

#{_libdir}/grilo-%{api}/grl-metadata-store.xml
%{_libdir}/grilo-%{api}/libgrlmetadatastore.so

#{_libdir}/grilo-%{api}/grl-opensubtitles.xml
%{_libdir}/grilo-%{api}/libgrlopensubtitles.so

#{_libdir}/grilo-%{api}/grl-podcasts.xml
%{_libdir}/grilo-%{api}/libgrlpodcasts.so

#{_libdir}/grilo-%{api}/grl-raitv.xml
%{_libdir}/grilo-%{api}/libgrlraitv.so

#{_libdir}/grilo-%{api}/grl-shoutcast.xml
%{_libdir}/grilo-%{api}/libgrlshoutcast.so

#{_libdir}/grilo-%{api}/grl-tracker.xml
%{_libdir}/grilo-%{api}/libgrltracker.so

#{_libdir}/grilo-%{api}/grl-vimeo.xml
%{_libdir}/grilo-%{api}/libgrlvimeo.so

#{_libdir}/grilo-%{api}/grl-youtube.xml
%{_libdir}/grilo-%{api}/libgrlyoutube.so

#{_libdir}/grilo-%{api}/grl-optical-media.xml
#{_libdir}/grilo-%{api}/libgrloptical-media.so

#{_libdir}/grilo-%{api}/grl-tmdb.xml
%{_libdir}/grilo-%{api}/libgrltmdb.so

#{_libdir}/grilo-%{api}/grl-freebox.xml
%{_libdir}/grilo-%{api}/libgrlfreebox.so

#{_libdir}/grilo-%{api}/grl-thetvdb.xml
#{_libdir}/grilo-%{api}/libgrlthetvdb.so

#{_libdir}/grilo-0.2/grl-daap.xml
#{_libdir}/grilo-0.2/grl-dpap.xml
#{_libdir}/grilo-0.2/libgrldaap.so
#{_libdir}/grilo-0.2/libgrldpap.so

#{_libdir}/%{name}-%{api}/libgrldaap.so


#{_libdir}/grilo-%{api}/grl-lua-factory.xml
#{_libdir}/grilo-%{api}/libgrlluafactory.so

#{_datadir}/%{name}/grl-lua-factory/grl-euronews.lua
#{_datadir}/%{name}/grl-lua-factory/grl-guardianvideos.lua
#{_datadir}/%{name}/grl-lua-factory/grl-metrolyrics.lua
#{_datadir}/%{name}/grl-lua-factory/grl-musicbrainz.lua
#{_datadir}/%{name}/grl-lua-factory/grl-radiofrance.lua
#{_datadir}/%{name}/grl-lua-factory/grl-appletrailers.gresource
#{_datadir}/%{name}/grl-lua-factory/grl-appletrailers.lua
#{_datadir}/%{name}/grl-lua-factory/grl-euronews.gresource
#{_datadir}/%{name}/grl-lua-factory/grl-guardianvideos.gresource
#{_datadir}/%{name}/grl-lua-factory/grl-pocket.gresource
#{_datadir}/%{name}/grl-lua-factory/grl-pocket.lua
#{_datadir}/%{name}/grl-lua-factory/grl-radiofrance.gresource
#{_datadir}/%{name}/grl-lua-factory/grl-video-title-parsing.lua
%{_datadir}/help/C/%{name}

%exclude /usr/lib/debug/usr/lib64/grilo-0.3/libgrldaap.so*
%exclude /usr/lib/debug/usr/lib64/grilo-0.3/libgrlopticalmedia.so*

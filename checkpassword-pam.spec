Summary:	The uniform PAM password-checking interface
Summary(pl):	Jednolite miêdzymordzie do hase³ PAM
Name:		checkpassword-pam
Version:	0.95
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://belnet.dl.sourceforge.net/sourceforge/checkpasswd-pam/checkpassword-pam-0.95.tar.gz
URL:		http://checkpasswd-pam.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
checkpassword provides a simple, uniform password-checking interface
to all root applications. It is suitable for use by applications such
as login, ftpd, and pop3d.

There are checkpassword-compatible tools that support alternate
password databases, secret login names, long passwords, subaccounts,
one-time passwords, detailed accounting, and many other features.
Applications that use the checkpassword interface will work with all
of these tools. Several tools have been specifically designed to
support POP toasters.

%description -l pl
Jednolite miêdzymordzie do hase³  umo¿liwiaj±ce wspó³dzia³anie
z bibliotek± PAM, do u¿ycia przez serwery takie jak
ftpd, pop3, imapd, login. 

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}
install checkpassword-pam $RPM_BUILD_ROOT%{_bindir}
install checkpassword-pam.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man8/*

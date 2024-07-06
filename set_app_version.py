import sys
import semver
import yaml


def get_previous_version(app_version: semver.Version) -> semver.Version:
    if app_version.major > 0:
        print("--bump=major")
        return semver.Version(
            major=app_version.major - 1,
            minor=app_version.minor,
            patch=app_version.patch,
            prerelease=app_version.prerelease,
            build=app_version.build,
        )
    elif app_version.minor > 0:
        print("--bump=minor")
        return semver.Version(
            major=app_version.major,
            minor=app_version.minor - 1,
            patch=app_version.patch,
            prerelease=app_version.prerelease,
            build=app_version.build,
        )
    else:
        print("--bump=patch")
        return semver.Version(
            major=app_version.major,
            minor=app_version.minor,
            patch=app_version.patch - 1,
            prerelease=app_version.prerelease,
            build=app_version.build,
        )


if __name__ == "__main__":
    tag_name = sys.argv[1]
    app_version = semver.Version.parse(tag_name.removeprefix("v"))
    previous_version = get_previous_version(app_version=app_version)

    with open("devvit.yaml", "r+") as fp:
        devvit_yaml = yaml.safe_load(fp)
        fp.seek(0)
        devvit_yaml["version"] = str(previous_version)
        yaml.safe_dump(devvit_yaml, fp)

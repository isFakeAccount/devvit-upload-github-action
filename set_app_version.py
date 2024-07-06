import sys
import semver
import yaml


def print_bump_flag(
    new_version: semver.Version, previous_version: semver.Version
) -> None:
    if new_version.major - previous_version.major == 1:
        print("--bump=major")
    elif new_version.minor - previous_version.minor == 1:
        print("--bump=minor")
    elif new_version.minor - previous_version.minor == 1:
        print("--bump=patch")
    else:
        raise ValueError(
            "Invalid version bump detected. Ensure that the version change follows Semantic Versioning rules, with only one of major, minor, or patch incremented by exactly 1."
        )


if __name__ == "__main__":
    tag_name = sys.argv[1]
    new_version = semver.Version.parse(tag_name.removeprefix("v"))

    with open("devvit.yaml", "r") as fp:
        devvit_yaml = yaml.safe_load(fp)
        current_version = semver.Version.parse(devvit_yaml["version"])

        if new_version.compare(current_version) <= 0:
            raise ValueError("New version must be greater than old version")

        print_bump_flag(new_version, current_version)

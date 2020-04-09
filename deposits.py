from typing import NamedTuple

# Before importing spec, load config:
from eth2spec.config.config_util import prepare_config
prepare_config("./", "minimal")

from eth2spec.phase0 import spec
from py_ecc.bls import G2ProofOfPossession as bls


print("genesis version:", spec.GENESIS_FORK_VERSION)


class DepositConfig(NamedTuple):
    privkey: str
    signing_root: str
    sig: str


configs = [
    DepositConfig(
        privkey="0x25295f0d1d592a90b333e26e85149708208e9f8e8bc18f6c77bd62f8ad7a6866",
        signing_root="139b510ea7f2788ab82da1f427d6cbe1db147c15a053db738ad5500cd83754a6",
        sig="b796b670fa7eb04b4422bb0872b016895a6adffb1ebd1023db41452701ad65d6fa53d84f3b62e8753bf55230364c6aa318620b574528506ad78517f70c688b82d1c9ad0b12633e0fa5792cf58c21cee9ad25f74156eebd0b6dcd548b91db860f"
    ),
    DepositConfig(
        privkey="0x51d0b65185db6989ab0b560d6deed19c7ead0e24b9b6372cbecb1f26bdfad000",
        signing_root="bb4b6184b25873cdf430df3838c8d3e3d16cf3dc3b214e2f3ab7df9e6d5a9b52",
        sig="98c4c6a7e12a2b4aeaa23a7d6ae4d2acabc8193d1c1cb53fabcb107ebcbd9c04189c4278995c62883507926712133d941677bd15407eefa49ea6c1cb97f4f7ee4efc3fe0bfa80e3efc3c6b48646b06e6bb845c4e0e7f21df58ef67147f0da7ea"
    ),
    DepositConfig(
        privkey="0x315ed405fafe339603932eebe8dbfd650ce5dafa561f6928664c75db85f97857",
        signing_root="c6ddd74b1b45db17a864c87dd941cb6c6e16540c534cdbe1cc0d43e9a5d87f7c",
        sig="8e6163059668ff2db1c8d430a1b0f9aeb330e8eaf680ed9709aaff5d437a54fb0144f2703cbb1e2a4a67c505b534718d0450d99203cccaf18e442bddd27e93ebfa289e6ce30a92e7befb656f12a01cb0204ffd14eed39ae457b7fad22faf8eab"
    ),
    DepositConfig(
        privkey="0x25b1166a43c109cb330af8945d364722757c65ed2bfed5444b5a2f057f82d391",
        signing_root="9397cd33d4e8883dbdc1a1d7df410aa2b627740d11c5574697a2d483a50ab7bb",
        sig="b389e7b4db5caccad6b0b32394b1e77a814e519f4d0789a1e4bb20e2f7f68d7787fe5f065181eeab72d31d847ae96abc0512466689eafbee0439ab7229fb14272654815f535759467e012d9ab7db6e3b3e86d9f73742c46993c755d1f2893684"
    ),
    DepositConfig(
        privkey="0x3f5615898238c4c4f906b507ee917e9ea1bb69b93f1dbd11a34d229c3b06784b",
        signing_root="27340cc0f3b76bcc89c78e67166c13a58c97c232889391d1387fc404c4f5255e",
        sig="aeb410612b19c3176fa087fab3e56e278a01cf5ba5379aa7f4e7344dbfa9e3b3f91b6f39af463ce2e448787b0a77ee1a05f22c0d9afd2f0f6137232c432f83c26389c07a8348364ab8a745eda59ecf2aa65fa8eb3f18eacd10e5a8a2e71b1e06"
    ),
    DepositConfig(
        privkey="0x055794614bc85ed5436c1f5cab586aab6ca84835788621091f4f3b813761e7a8",
        signing_root="b8cf48542d8531ae59b56e175228e7fcb82415649b5e992e132d3234b31dda2f",
        sig="b501a41ca61665dddbe248d2fa15e5498cb2b38dcf2093acd5768efeda1b0ac963e600d8e38c2c91964d8bf72fd197c71824c1d493272caf6140828f7f6b266281f044b4811bbd7ef0f57953b15399b4ef17af5b9c80df5c142600cf17bfee64"
    ),
    DepositConfig(
        privkey="0x1023c68852075965e0f7352dee3f76a84a83e7582c181c10179936c6d6348893",
        signing_root="5f919d91faecece67422edf573a507fc5f9720f4e37063cceb40aa3b371f1aa9",
        sig="8f2e2de3c0504cc4d424de1593d508d7488bfc54f61882922b754e97e4faeebe4f24f19184f0630dc51327bc9ab26dd2073d55687f7284ab3395b770d7c4d35bb6e719e6881739e2f4f61e29e11c3b9e61529c202e30f5f5957544eeb0a9626e"
    ),
    DepositConfig(
        privkey="0x3a941600dc41e5d20e818473b817a28507c23cdfdb4b659c15461ee5c71e41f5",
        signing_root="d2ff8bfda7e7bcc64c636a4855d2a1eccb7f47379f526a753fd934ae37ba9ec7",
        sig="90a83842b6d215f1da3ebf3eeea6c4bff0682ee3f7aa9d06bb818c716cfdb5cd577f997ddd606c908f7a68157f36ff660a0e73265f17cccbd23be5ed053b3812672ba52bce6ec034fadea3b78f46a9c6da88db6327a18a9bb3a7f2747185fc6f"
    ),
    DepositConfig(
        privkey="0x066e3bdc0415530e5c7fed6382d5c822c192b620203cf669903e1810a8c67d06",
        signing_root="1e19687d32785632ddc9b6b319690ea45c0ea20d7bc8aacbd33f6ebbe30816e1",
        sig="a232a8bb03ecd356cf0e18644077880afe7ecfc565c8627841797deb4dfce8366cc0d0f6e151b51c0acc05a66f1363d204e8133e772dfb4878c11f7bf14b8293ce734c37adca9c32cc2987f0bc34242cc30f139d86c44f8d4383af743be3d1ae"
    ),
    DepositConfig(
        privkey="0x2b3b88a041168a1c4cd04bdd8de7964fd35238f95442dc678514f9dadb81ec34",
        signing_root="64a910a0a3e7da9a7a29ee2c92859314a160040ffb2042641fc56cba75b78012",
        sig="8e0ccf7dd9dd00820a695161ea865220489ca48504012b7c36c85b3effb896a02ee9714a5e383f7105357a24f791562c1353e331d2cfa048cb94fd4fe42a008b18c5bdec6fcf7c8b75c5f5e582cd9571b308e8b1757d672fbb9092725985a716"
    ),
    DepositConfig(
        privkey="0x2e62dbea7fe3127c3b236a92795dd633be51ee7cdfe5424882a2f355df497117",
        signing_root="5bf0c7a39df536b3c8a5dc550f0163af0b33a56b9454b5240cea9ad8356c4117",
        sig="a07adeeb639a974fe3ae78a0a28785b195bffeaa2ec558c6baa63458daaf5b7a245940a2d9b91a993515295075eba4e115c6777eda1e7933cb53f64ab36619e49faadf289a8cc1521ca3ae5f9a3f2b88e355ef0b75dd8a9949c9d2a43c5589e0"
    ),
    DepositConfig(
        privkey="0x2042dc809c130e91906c9cb0be2fec0d6afaa8f22635efc7a3c2dbf833c1851a",
        signing_root="e8a45fa71addd854d8d78e0b2cdc8f9100c8a5e03d894c1c382068e8aa4b71e2",
        sig="95719c0c4dae737aac602aeadf9faeb9ad3492450af249c43a1147a6e471ddb3f2b5979b6587e843d20c9caa8ecd83e8001b57a4f7c302927725966acc959eb6668357831b7a0692f2396a18939d9fa974e611beed4a7a59ffe892e77d2680bd"
    ),
    DepositConfig(
        privkey="0x15283c540041cd85c4533ee47517c8bb101c6207e9acbba2935287405a78502c",
        signing_root="3dfab0daa3be9c72c5dd3b383e756d6048bb76cd3d09abb4dc991211ae8a547b",
        sig="b8221ad674d7c23378b488555eb6e06ce56a342dad84ba6e3a57e108c1c426161b568a9366d82fd0059a23621922a1fc0e59d8eaa66dbb4611a173be167731367edf8daad3b07b64207faf3ea457a335228def3ca61571c4edc15dc392bf4e56"
    ),
    DepositConfig(
        privkey="0x03c85e538e1bb30235a87a3758c5571753ca1308b7dee321b74c19f78423999b",
        signing_root="8905ae60c419e38f263eb818a5536e4144df3c0a800132e07594d457c62b5825",
        sig="a5e61349958745c80862af84e06924748832cae379b02a50909468fef9f07f21d35a98e1287b6219528a1ad566567d0619e049efa9fa6e81410bb3a247cf53b0f6787f747f8229fb9f851290b140f14f14a2adcb23b7cafaf90b301d14169324"
    ),
    DepositConfig(
        privkey="0x45a577d5cab31ac5cfff381500e09655f0799f29b130e6ad61c1eec4b15bf8dd",
        signing_root="702d1bd9c27c999923149f6c6578c835943b58b90845086bbf5be3b94aa4663d",
        sig="893d8e70f2cdb6f7acc3d9828e72d7b20e512956588d8c068b3ef4aa649db369cf962506b7c9107246246d9b20361cd80250109da513809415314af3ef1f220c171dbc2d9c2b62056739703ae4eb1be13fa289ea8472920b2393041f69198dc5"
    ),
    DepositConfig(
        privkey="0x03cffafa1cbaa7e585eaee07a9d35ae57f6dfe19a9ea53af9c37e9f3dfac617c",
        signing_root="77f3da02c410e9ccba39d89983c52e6e77ca5dec3ae423311a578ee28b2ec0cd",
        sig="87ae1567999d3ceefce04c1a48aa189c3d368efbeda53c01962783941c03d3a26e08e5e9d287a927decf4e77755b97e80856e339c3af41dc5ffd373c6e4768de62718ce76cfd8c2062e7673c9eedd2fec235467967f932e59e0b3a32040c0038"
    )
]

amount = spec.MAX_EFFECTIVE_BALANCE

datas = []
for i, c in enumerate(configs):
    print(f"----------- deposit {i} --------------", i)
    privkey = int.from_bytes(bytes.fromhex(c.privkey.replace('0x', '')), byteorder='big')
    pubkey = bls.PrivToPub(privkey)
    print("priv", privkey.to_bytes(length=32, byteorder='big').hex())
    print("pub", pubkey.hex())

    # insecurely use pubkey as withdrawal key if no credentials provided
    withdrawal_credentials = spec.BLS_WITHDRAWAL_PREFIX + spec.hash(pubkey)[1:]
    print("withdrawal creds", withdrawal_credentials.hex())

    deposit_message = spec.DepositMessage(
        pubkey=pubkey,
        withdrawal_credentials=withdrawal_credentials,
        amount=amount,
    )
    print("dep message root", deposit_message.hash_tree_root().hex())

    domain = spec.compute_domain(spec.DOMAIN_DEPOSIT)
    signing_root = spec.compute_signing_root(deposit_message, domain)
    print("sig root", signing_root.hash_tree_root().hex())

    signature = bls.Sign(privkey, signing_root)
    print("computed signature: ", signature.hex())
    print("  client signature: ", c.sig)

    deposit_data = spec.DepositData(
        pubkey=pubkey,
        withdrawal_credentials=withdrawal_credentials,
        amount=amount,
        signature=signature,
    )
    print("dep data root", deposit_data.hash_tree_root().hex())
    datas.append(deposit_data)

print("-------------")

deposit_data_list = spec.List[spec.DepositData, 2**spec.DEPOSIT_CONTRACT_TREE_DEPTH](*datas)

print(deposit_data_list.hash_tree_root().hex())

def print_node(node, depth):
    indent = ('%5d' % depth) + '  ' * depth
    if node.is_leaf():
        print(indent + node.root.hex())
    else:
        print(indent + node.root.hex() + ' -> (')
        print_node(node.left, depth + 1)
        print_node(node.right, depth + 1)
        print(indent + ')')


print_node(deposit_data_list.get_backing(), 0)


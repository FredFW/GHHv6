from subprocess import Popen, PIPE
import protocol

class Guest:
    def __init__(self):
        self.proc = None

    def __enter__(self):
        self.proc = Popen(
            'qemu-system-x86_64 -boot d -cdrom kernel_bios.iso -m 300M -serial stdio -enable-kvm',
            stdout=PIPE, stdin=PIPE, shell=True
            )
        return self

    def __exit__(self, type, value, traceback):
        self.proc.kill()

    def messages(self):
        while self.proc.returncode is None:
            yield protocol.recv(self.proc.stdout)

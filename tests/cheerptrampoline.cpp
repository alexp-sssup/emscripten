#include <cheerp/clientlib.h>

namespace client
{
	class [[cheerp::genericjs]] Module
	{
	public:
		Array* get_preRun();
		Array* get_postRun();
	};

	[[cheerp::genericjs]]
	extern Module* Module;
}

extern int main(int argc, const char* argv[]);

#define EMBENCHEN 0

void webMain()
{
	const char* args[2];
	args[0]="benchmark";
	args[1]="4";
	const char** a=&args[0];
#if EMBENCHEN
	if(client::Module->get_preRun())
	{
		client::Array& preRun=*client::Module->get_preRun();
		for(int i=0;i<preRun.get_length();i++)
			reinterpret_cast<void(*)()>(preRun[i])();
	}
#endif
	volatile int exit_code = main(2, a);
#if EMBENCHEN
	if(client::Module->get_postRun())
	{
		client::Array& postRun=*client::Module->get_postRun();
		for(int i=0;i<postRun.get_length();i++)
			reinterpret_cast<void(*)()>(postRun[i])();
	}
#endif
}

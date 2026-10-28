from lab.main import main


def test_main_runs(capsys) -> None:
    main()
    assert "Replace" in capsys.readouterr().out

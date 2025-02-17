import typer
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = typer.Typer()
Base = declarative_base()


class Memo(Base):
    __tablename__ = "memos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String, nullable=False)


engine = create_engine("sqlite:///memos.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


@app.command()
def add(content: str):
    """Add a new memo."""
    session = Session()
    new_memo = Memo(content=content)
    session.add(new_memo)
    session.commit()
    session.close()
    typer.echo("Memo added!")


@app.command()
def list():
    """List all memos."""
    session = Session()
    memos = session.query(Memo).all()
    session.close()
    for memo in memos:
        typer.echo(f"{memo.id}: {memo.content}")


@app.command()
def delete(memo_id: int):
    """Delete a memo by its ID."""
    session = Session()
    memo = session.query(Memo).filter(Memo.id == memo_id).first()
    if memo:
        session.delete(memo)
        session.commit()
        typer.echo("Memo deleted!")
    else:
        typer.echo("Memo not found!")
    session.close()


if __name__ == "__main__":
    app()
